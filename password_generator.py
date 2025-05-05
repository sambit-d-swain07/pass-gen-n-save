import os
import random
import string
import re
from cryptography.fernet import Fernet
from datetime import datetime
from colorama import Fore, Style, init
import pyfiglet

init(autoreset=True)

# --- Fancy Title and Footer ---
def print_title():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + pyfiglet.figlet_format("Pass Gen N Save", font="slant"))
    print(Fore.YELLOW + "="*60)
    print("Made by Sambit D Swain".center(60))
    print(Fore.YELLOW + "="*60 + "\n")

def print_menu():
    print(Fore.GREEN + "1. 🔐 Generate a Strong Password")
    print(Fore.MAGENTA + "2. 🔓 Decrypt a Saved Password")
    print(Fore.RED + "3. ❌ Exit\n")

# --- Password Functions ---
def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def check_password_strength(password):
    if len(password) < 12:
        return "Weak"
    tests = [r'[A-Z]', r'[a-z]', r'[0-9]', r'[!@#$%^&*(),.?":{}|<>]']
    return "Strong" if all(re.search(p, password) for p in tests) else "Medium"

def encrypt_password(password, key):
    return Fernet(key).encrypt(password.encode())

def decrypt_password(encrypted_password, key):
    try:
        return Fernet(key).decrypt(encrypted_password).decode()
    except:
        return None

# --- File Saving Helpers ---
def save_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)

def read_file(filename):
    with open(filename, 'rb') as f:
        return f.read()

def generate():
    os.makedirs("passwords", exist_ok=True)
    length = input("Enter password length (default 16): ")
    length = int(length) if length.isdigit() else 16

    password = generate_password(length)
    strength = check_password_strength(password)
    key = Fernet.generate_key()
    encrypted = encrypt_password(password, key)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    pfile = f"passwords/encrypted_{timestamp}.txt"
    kfile = f"passwords/key_{timestamp}.txt"
    logfile = "passwords/password_index.txt"

    save_file(encrypted, pfile)
    save_file(key, kfile)

    with open(logfile, 'a') as log:
        log.write(f"{timestamp} - Strength: {strength} - {pfile} - {kfile}\n")

    print(Fore.CYAN + "\nPassword Generated:")
    print(Fore.GREEN + f"{password}")
    print(Fore.YELLOW + f"\n🔐 Encrypted saved to: {pfile}")
    print(Fore.BLUE + f"🗝️  Key saved to: {kfile}")
    print(Fore.WHITE + "📒 Log updated!\n")

def decrypt():
    print(Fore.CYAN + "\nDecrypt a Password:")
    enc_path = input("📄 Enter encrypted password file path: ").strip()
    key_path = input("🗝️  Enter key file path: ").strip()

    try:
        encrypted = read_file(enc_path)
        key = read_file(key_path)
        decrypted = decrypt_password(encrypted, key)

        if decrypted:
            print(Fore.GREEN + f"\n✅ Decrypted password: {decrypted}\n")
        else:
            print(Fore.RED + "\n❌ Invalid key or corrupted file.\n")
    except Exception as e:
        print(Fore.RED + f"\n❌ Error: {e}\n")

# --- Main App ---
def main():
    while True:
        print_title()
        print_menu()
        choice = input(Fore.WHITE + "\nEnter your choice (1/2/3): ").strip()

        if choice == '1':
            print_title()
            generate()
        elif choice == '2':
            print_title()
            decrypt()
        elif choice == '3':
            print(Fore.RED + "\n👋 Exiting... Stay safe!\n")
            break
        else:
            print(Fore.RED + "\n❗ Invalid choice, try again.\n")

        input(Fore.WHITE + "Press Enter to return to menu...")

if __name__ == "__main__":
    main()

