
with open("key.txt") as keyfile:
    key = keyfile.read()
iv = "0000111122223333"
with open("plain.bmp", "rb") as f:
    clear = f.read()
header, body = clear[:54], clear[54:]
length = len(key) - 1
print(length)
ciphertext = bytes()
for i in range(0, len(body), length):
    block = bytes(body[i:i + length])
    encoded = bytes()
    for j in range(0, 16):
        xored = block[j] ^ ord(key[j])
        xored2 = xored.to_bytes(1, "big")
        encoded = encoded + xored2
    ciphertext = ciphertext + encoded
ciphertext = header + ciphertext
with open("ecb_crypto.bmp", "wb") as f:
    f.write(ciphertext)
iv = bytes(iv, "utf-8")
ciphertext2 = bytes()
for i in range(0, len(body), length):
    block = body[i:i + length]
    encoded = bytes()
    for j in range(0, 16):
        xored = block[j] ^ iv[j]
        xored2 = xored ^ ord(key[j])
        xored3 = xored2.to_bytes(1, "big")
        encoded = encoded + xored3
    ciphertext2 = ciphertext2 + encoded
    iv = encoded
ciphertext2 = header + ciphertext2
with open("cbc_crypto.bmp", "wb") as f:
    f.write(ciphertext2)
