from Crypto.Cipher import AES
key = "aaaabbbbccccdddd"
key2 = bytes(key, "utf-8")
cipher = AES.new(key2, AES.MODE_ECB)
with open("hand.bmp", "rb") as f:
    clear = f.read()
clear_trimmed = clear[128:-8]
ciphertext = cipher.encrypt(clear_trimmed)
ciphertext = clear[0:128] + ciphertext + clear[-8:]
with open("hand_ecb.bmp", "wb") as f:
    f.write(ciphertext)
