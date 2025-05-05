decryptor tool. Includes encryption, password strength check, and indexed secure storage.

📄 README.md
markdown
Copy
Edit
# 🔐 Pass Gen N Save

**Pass Gen N Save** is a stylish, secure, and terminal-based password manager. It lets you:
- ✅ Generate strong, unique passwords
- 🔐 Encrypt and store them securely
- 🔓 Decrypt saved passwords later with ease
- 🎨 Navigate a beautifully styled terminal UI

---

## ✨ Features

- Colorful and user-friendly terminal design using `colorama` and `pyfiglet`
- Automatically saves each password and encryption key to separate files
- Password strength checker (Weak / Medium / Strong)
- Maintains a full password index log (`password_index.txt`)
- Made with ❤️ by **Sambit D Swain**

---

## 🧩 Requirements

Install dependencies:

```bash
pip install cryptography colorama pyfiglet
🚀 How to Use
🔧 Run the Tool
bash
Copy
Edit
python pass_gen_n_save.py
🧭 Main Menu
css
Copy
Edit
1. 🔐 Generate a Strong Password
2. 🔓 Decrypt a Saved Password
3. ❌ Exit
🛠️ Password Generation
Generates a strong password (default: 16 characters)

Shows strength level

Encrypts and saves:

passwords/encrypted_YYYYMMDD_HHMMSS.txt

passwords/key_YYYYMMDD_HHMMSS.txt

Adds a log entry to passwords/password_index.txt

🗂️ Where are my passwords saved?
All files are saved in a directory called:

pgsql
Copy
Edit
passwords/
├── encrypted_*.txt   ← Encrypted password files
├── key_*.txt         ← Corresponding encryption keys
└── password_index.txt ← Master log of all generated entries
🔓 Password Decryption
Choose option 2 from the menu

Enter the path to your encrypted password file and key file

The original password is decrypted and displayed

🔐 Security Tips
Keep your key files private and secure

Use a password manager or backup location

Never share your encryption key or decrypted passwords

👨‍💻 Author
Made by Sambit D Swain

📜 License
MIT License – free for personal and commercial use.

yaml
Copy
Edit
