import hashlib
import os
import platform
import subprocess
import sys
import urllib.request
def download_wordlist():
    print('''
     
##      ##  #######  ########  ########  ##       ####  ######  ########     ######   ######## ##    ## ######## ########     ###    ########  #######  ########  
##  ##  ## ##     ## ##     ## ##     ## ##        ##  ##    ##    ##       ##    ##  ##       ###   ## ##       ##     ##   ## ##      ##    ##     ## ##     ## 
##  ##  ## ##     ## ##     ## ##     ## ##        ##  ##          ##       ##        ##       ####  ## ##       ##     ##  ##   ##     ##    ##     ## ##     ## 
##  ##  ## ##     ## ########  ##     ## ##        ##   ######     ##       ##   #### ######   ## ## ## ######   ########  ##     ##    ##    ##     ## ########  
##  ##  ## ##     ## ##   ##   ##     ## ##        ##        ##    ##       ##    ##  ##       ##  #### ##       ##   ##   #########    ##    ##     ## ##   ##   
##  ##  ## ##     ## ##    ##  ##     ## ##        ##  ##    ##    ##       ##    ##  ##       ##   ### ##       ##    ##  ##     ##    ##    ##     ## ##    ##  
 ###  ###   #######  ##     ## ########  ######## ####  ######     ##        ######   ######## ##    ## ######## ##     ## ##     ##    ##     #######  ##     ## 
    ''')
    if os.path.exists("wordlist.txt"):
        print("Wordlist already exists")
        return
    url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"
    print("Downloading wordlist...")
    try:
        urllib.request.urlretrieve(url, "wordlist.txt")
    except:
        print("Failed to download wordlist.")
        return None
    print("Wordlist downloaded.")
    return 
download_wordlist()