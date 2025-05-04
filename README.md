# PRODIGY_CS_01
A Python tool for encrypting and decrypting messages using the Caesar Cipher technique.

# Caesar Cipher - Text Encryption and Decryption Tool

## Description

This is a simple Python implementation of the Caesar Cipher encryption and decryption technique. It allows users to input a message and a shift value (key) to perform letter substitution. The Caesar Cipher is a classical encryption method where each letter in the message is shifted by a fixed number of positions in the alphabet. This tool supports both uppercase and lowercase letters while preserving numbers, symbols, and spacing. It demonstrates the fundamentals of classical cryptography using Python.

---

## Objective

- To demonstrate the concept of substitution ciphers.
- To build a working Caesar Cipher tool with encryption and decryption modes.
- To reinforce understanding of modular arithmetic, ASCII values, and character handling in Python.

---

## Requirements

- Python 3.x

No external libraries are required.

---

## How to Use

1. Clone or download this repository.
2. Run the script using Python:

```bash
python caesar_cipher.py
```

3. Follow the on-screen prompts:
   - Choose encryption or decryption
   - Enter your message
   - Enter the shift value (key)

---

## Example

```bash
==== Caesar Cipher Encryption/Decryption ====
1. Encrypt a message
2. Decrypt a message
Choose an option (1/2): 1
Enter your message: Hello, World!
Enter shift value: 3
Encrypted Message: Khoor, Zruog!
```

---

## Files

- `caesar_cipher.py` – Main Python script
- `README.md` – Project documentation

---

## Note

This cipher is not secure for real-world applications. It is vulnerable to brute-force attacks due to its limited keyspace.

---
