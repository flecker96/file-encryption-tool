# 🔐 Secure File Encryption Tool (AES-GCM)

A lightweight, secure file encryption tool built in Python using modern authenticated encryption.

This project demonstrates applied cryptography and secure system design.

It implements file encryption using Advanced Encryption Standard in Galois/Counter Mode (GCM) with password-based key derivation.

## ✨ Features

🔐 AES-256-GCM authenticated encryption (confidentiality + integrity)

🔑 Password-based key derivation using PBKDF2

🧂 Random salt generation for secure key separation

🛡️ Tamper detection via authentication tags

💻 Command-line interface (CLI)

📦 Simple binary file format for portability

## ⚙️ How it works

### 1. Key derivation

A password is converted into a cryptographic key using:

PBKDF2 (Password-Based Key Derivation Function 2)
SHA-256
200,000 iterations
Random salt

This ensures brute-force resistance and uniqueness per encryption.

### 2. Encryption

Data is encrypted using AES-GCM:

Random 96-bit nonce
Authenticated encryption (prevents tampering)
Outputs ciphertext + authentication tag

### 3. File format

Each encrypted file has the structure:

[salt (16 bytes)] + [nonce + ciphertext + tag]

## 🚀 Installation
```
pip install cryptography
```
## 📦 Usage

Run from project root:

🔐 Encrypt a file
```
PYTHONPATH=src python -m sfe.cli encrypt input.txt output.enc -p mypassword
```
🔓 Decrypt a file
```
PYTHONPATH=src python -m sfe.cli decrypt output.enc decrypted.txt -p mypassword
```
🧪 Example
```
echo "secret message" > test.txt

PYTHONPATH=src python -m sfe.cli encrypt test.txt test.enc -p test123
PYTHONPATH=src python -m sfe.cli decrypt test.enc out.txt -p test123

```
## 💻 Command Line Interface (CLI)

Alternatively, this tool also provides a command-line interface which makes the command for en-/decryption more convenient.

🔧 Installation (required)
```
pip install -e .
```
Now the sfe command becomes available.

🔐 Encrypt a file
```
sfe encrypt <input_file> <output_file> -p <password>
```
🔓 Decrypt a file
```
sfe decrypt <input_file> <output_file> -p <password>
```

## 🔐 Security Design Notes
✔ Encryption mode

Uses AES-GCM, which provides:

Confidentiality (encryption)
Integrity (tamper detection)
Authenticity (prevents forgery)

✔ Key derivation

Passwords are never used directly as encryption keys.

Instead, they are processed using PBKDF2 with:

Random salt
High iteration count (200,000)

This slows down brute-force attacks significantly.

## ⚠️ Security assumptions
Security depends on password strength.

Nonce must never be reused with the same key.


## 🧱 Project Structure
```
src/
└── sfe/
    ├── cli.py
    ├── crypto.py
    ├── kdf.py
    ├── utils.py
    ├── exceptions.py
    └── __init__.py
```

## 📌 Limitations
No key management system (password-based only)

Not optimized for large-scale distributed systems

No hardware security module (HSM) integration

Educational implementation using standard libraries


## 👤 Author

PhD in Theoretical Physics

Focus: computational physics, complex systems, numerical relativity

Interested in:

Applied cryptography,
Secure system design,
Space/ground communication architectures
