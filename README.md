# Cryptography
## Cryptography in Python
This repository will show Python implementations of various ciphers. 
## Block ciphers
The block.py file simulates block ciphers ECB (Electronic Code Book) and CBC (Cipher Block Chaining) by encrypting an image.
The user needs to create a key (16 ASCII chars) and find an image. After running the script with 
```python block.py``` the user will be able to understand, why ECB is not
used. CBC is one of the first blockchains (used in cryptocurrencies like Bitcoin).
In the future Caesar and affine ciphers are to be added.
## Enigma I
enigmaI.py simulates German encoding machine Enigma. It was widely used in Germany in the 1920s and 1930s. The code was broken in 1932 by Polish mathematicians Marian Rejewski, Jerzy Różycki and Henryk Zygalski.
The script can be run with the command
```python enigmaI.py```
