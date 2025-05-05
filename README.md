# 🔐 Pass Gen N Save

**Pass Gen N Save** is a stylish, secure, and terminal-based password tool that helps you:
- ✅ Generate strong, encrypted passwords
- 🔓 Decrypt previously saved passwords
- 🧾 Automatically keep a log of all generated passwords
- 💻 Use a clean, colorful interface for better experience

> **Made by Sambit D Swain**

---

## 🚀 Features

- 💡 **Strong Password Generation** (custom length)
- 🔐 **AES Encryption** with Fernet (via `cryptography`)
- 🗂️ **Secure Password Storage** (timestamped files)
- 📋 **Index Log File**: Tracks all generated passwords
- 🖥️ **Colorful CLI UI** with `colorama` and `pyfiglet`

---

## 📦 Installation

Install required libraries:

```bash
pip install cryptography colorama pyfiglet
🧭 How to Use
▶️ Run the Tool
bash

python pass_gen_n_save.py
You will see a colorful welcome screen like this:



Edit![Screenshot 2025-05-05 191444](https://github.com/user-attachments/assets/d37e9c78-d812-4c39-853f-8b636236b36e)


📘 Option Guide
🔐 Option 1: Generate a Strong Password
Enter a custom length (or press Enter for default 16)

A secure password is generated with:

Uppercase, lowercase, numbers, and symbols

Password is encrypted with a unique key

Two files are saved:

🔐 passwords/encrypted_YYYYMMDD_HHMMSS.txt

🗝️ passwords/key_YYYYMMDD_HHMMSS.txt

A log entry is also created in:

📒 passwords/password_index.txt

💬 Example:


✅ Password: n#8uA3$Rd!lJmZ1p
🔐 Encrypted saved to: passwords/encrypted_20250504_143010.txt
🗝️  Key saved to: passwords/key_20250504_143010.txt
📒 Entry added to log: passwords/password_index.txt
🔓 Option 2: Decrypt a Saved Password
To retrieve a previously saved password:

Select option 2

Enter the full path to the:

🔐 Encrypted password file

🗝️ Key file

The tool will decrypt and show the original password

💬 Example:

📄 Enter encrypted password file path: passwords/encrypted_20250504_143010.txt
🗝️  Enter key file path: passwords/key_20250504_143010.txt
✅ Decrypted password: n#8uA3$Rd!lJmZ1p
❌ Option 3: Exit
Cleanly exits the tool with a goodbye message.

📁 Password Storage Structure
When you generate a password, files are saved inside the passwords/ folder:

passwords/
├── encrypted_YYYYMMDD_HHMMSS.txt   # Encrypted password
├── key_YYYYMMDD_HHMMSS.txt         # Encryption key
├── password_index.txt              # Log of all passwords
Each file is timestamped to prevent overwriting

You can track all saved entries in password_index.txt

🛡️ Security Tips
Never share your key files publicly

Store the passwords/ folder in a safe place

Consider backing up password_index.txt securely

Avoid decrypting passwords on untrusted systems

👤 Author
Made with ❤️ by Sambit D Swain
