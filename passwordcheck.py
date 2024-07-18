import os
import platform
import subprocess
import sys
import urllib.request
print('''
8888888b.                                                               888       .d8888b.  888                        888      
888   Y88b                                                              888      d88P  Y88b 888                        888      
888    888                                                              888      888    888 888                        888      
888   d88P 8888b.  .d8888b  .d8888b  888  888  888  .d88b.  888d888 .d88888      888        88888b.   .d88b.   .d8888b 888  888 
8888888P"     "88b 88K      88K      888  888  888 d88""88b 888P"  d88" 888      888        888 "88b d8P  Y8b d88P"    888 .88P 
888       .d888888 "Y8888b. "Y8888b. 888  888  888 888  888 888    888  888      888    888 888  888 88888888 888      888888K  
888       888  888      X88      X88 Y88b 888 d88P Y88..88P 888    Y88b 888      Y88b  d88P 888  888 Y8b.     Y88b.    888 "88b 
888       "Y888888  88888P'  88888P'  "Y8888888P"   "Y88P"  888     "Y88888       "Y8888P"  888  888  "Y8888   "Y8888P 888  888                                                                                                                                                                                                                          
''')
with open("wordlist.txt", "r", encoding="utf-8") as f:
    cracked_password=None
    actual_password=input("Enter the password : ")
    for pwd in f:
        pwd=pwd.strip()
        if pwd == actual_password:
            cracked_password = pwd
            break
if cracked_password:
    print(f"Password cracked: {cracked_password}")
else:
    print("Password not found in common passwords list.")
    print("Congrats your password is not common ")