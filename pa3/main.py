from pa3 import *

def main():
    text = "STOP POLLUTION"
    n = 3589
    e = 17
    cipher = affine_encrypt(text, 1, 5)
    print(f"Test: {text} Cipher = {cipher}")
    de_cipher = affine_decrypt(cipher, 1, 5)
    print(f"Text_encrypt: {cipher}  Text: {de_cipher}")
    rsa_en = rsa_encrypt(text, n, e)
    print(f"\nText: {text}  RSA Encryption: {rsa_en}")

main()