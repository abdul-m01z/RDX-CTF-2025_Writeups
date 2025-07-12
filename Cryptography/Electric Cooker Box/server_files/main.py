from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

KEY = os.urandom(16)
with open("flag.txt", "r") as flagFileHandle:
    FLAG = flagFileHandle.read().strip().encode()

def aes_ecb_encrypt(plaintext: bytes):
    cipher = AES.new(KEY, AES.MODE_ECB)
    padded = pad(plaintext + FLAG, 16)
    return cipher.encrypt(padded)


while True:
    try:
        plaintext = input("\n[?] Enter plaintext: ").encode()
        ciphertext = aes_ecb_encrypt(plaintext)
        print(f"[+] Ciphertext (Hex): {ciphertext.hex()}")
    except:
        print("\n[-] Invalid Input - TERMINATING SESSION")
        exit()