import hashlib
import os
import platform
import subprocess
import sys
import urllib.request

HASH_FUNCTIONS = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
    "sha512": hashlib.sha512,
}

def main():
    while True:
        print_ascii_cat("Hash Cracker")
        print("1. Crack a hash\n2. Exit")
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == "1":
            hash_to_crack = input("Enter the hash to crack: ")
            hash_function = select_hash_function()
            encoding = input("Enter the character encoding of the wordlist (press Enter for default UTF-8): ") or "utf-8"
            try:
                with open("wordlist.txt", "r", encoding=encoding) as f:
                    for word in f:
                        word = word.strip()
                        hashed_word = hash_function(word.encode(encoding)).hexdigest()
                        if hashed_word == hash_to_crack:
                            print(f"Hash cracked: {word}")
                            break
                    else:
                        print("Hash not found in wordlist.")
                        
            except Exception as e:
                print(f"An error occurred: {e}")
                if input("Press 'Enter' to return to the main menu or 'q' to quit: ") == 'q':
                    break
                
        elif choice == "2":
            break
            
        else:
            print("Invalid choice. Please enter 1 or 2.")
            
    print("Goodbye!")

def print_ascii_cat(tool_name):
    print(r'''
 | |  | |         | |     |  __ \                   | |          
 | |__| | __ _ ___| |__   | |  | | ___  ___ ___   __| | ___ _ __ 
 |  __  |/ _` / __| '_ \  | |  | |/ _ \/ __/ _ \ / _` |/ _ \ '__|
 | |  | | (_| \__ \ | | | | |__| |  __/ (_| (_) | (_| |  __/ |   
 |_|  |_|\__,_|___/_| |_| |_____/ \___|\___\___/ \__,_|\___|_|  ''', tool_name, "\n")

def select_hash_function():
    while True:
        print("Select the hash function to use:")
        for i, function_name in enumerate(HASH_FUNCTIONS):
            print(f"{i+1}. {function_name}")
        choice = input("Enter your choice (1-4): ")
        try:
            index = int(choice) - 1
            function_name = list(HASH_FUNCTIONS.keys())[index]
            return HASH_FUNCTIONS[function_name]
        except (IndexError, ValueError):
            print("Invalid choice. Please enter a number from 1-4.")



if __name__ == "__main__":
    main()
