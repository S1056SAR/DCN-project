from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64
def encrypt(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct
print('''
    ###    ########  ######  
  ## ##   ##       ##    ## 
 ##   ##  ##       ##       
##     ## ######    ######  
######### ##             ## 
##     ## ##       ##    ## 
##     ## ########  ######  
''')
key = get_random_bytes(16)  
actual_password = input("Enter your password: ")
iv, encrypted_password = encrypt(actual_password, key)
print(f"Encrypted password: {encrypted_password}")
print("\nAES encryption makes the password unreadable without the key.")
print("Even with brute force attempts, without the key, the encrypted data cannot be decrypted.")
