import subprocess

def main_menu():
    while True:
        print('''
         _  _   _      _____   ___   _   _    _    _____  ___     ____     _     ___    ___  __   __ ____   ____   ___     _____  ____   ____   _     
) () ( ) |    )__ __( )_ _( ) \_/ (  )_\  )__ __() __(   )  _)\   )_\   (  _(  (  _( ) (_) (/ __ \ /  _ \ \   \   )__ __(/ __ \ / __ \ ) |    
| \/ | | (__    | |   _| |_ |  _  | /( )\   | |  | _)    | '__/  /( )\  _) \   _) \  \  _  /))__(( )  ' / | ) (     | |  ))__(( ))__(( | (__  
)____( )____(   )_(  )_____()_( )_()_/ \_(  )_(  )___(   )_(    )_/ \_()____) )____)  )/ \( \____/ |_()_\ /___/     )_(  \____/ \____/ )____(
        ''')
        print("1. Wordlist Generator")
        print("2. Password Checker")
        print("3. Hash Decoder")
        print("4. Encryption using AES")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            subprocess.run(["python", "wordlistgen.py"])
        elif choice == "2":
            subprocess.run(["python", "passwordcheck.py"])
        elif choice == "3":
            subprocess.run(["python", "hash.py"])
        elif choice == "4":
            subprocess.run(["python", "encrypt.py"])
        elif choice == "5":
            print("Exiting the menu.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main_menu()
