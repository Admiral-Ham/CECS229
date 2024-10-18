from pa3 import *

def main():
    text = "REPEAT"
    n = 2537
    e = 13
    cipher = affine_encrypt(text, 1, 5)
    print(f"Test: {text} Cipher = {cipher}")
    de_cipher = affine_decrypt(cipher, 1, 5)
    print(f"Text_encrypt: {cipher}  Text: {de_cipher}")
    rsa_en = rsa_encrypt(text, n, e)
    print(f"\nText: {text}  RSA Encryption: {rsa_en}")

main()