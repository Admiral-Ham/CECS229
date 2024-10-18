from pa3 import *

def main():
    message = "Hello"
    cipher = affine_encrypt(message, 1, 5)
    print(f"Test: {message} Cipher = {cipher}")
    de_cipher = affine_decrypt(cipher, 1, 5)
    print(f"Text_encrypt: {cipher}  Text: {de_cipher}")

main()