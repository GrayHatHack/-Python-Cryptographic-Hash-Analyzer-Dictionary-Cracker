# 🔓 Python Cryptographic Hash Analyzer & Dictionary Cracker

A foundational security tool built to understand password hashing mechanics, cryptographic digests, and simulated dictionary/brute-force attacks in penetration testing.

## 🚀 Features
- **Hash Generation (`hash_tool.py`):** Computes cryptographic checksums (MD5 and SHA-256) for user-provided text input using Python's `hashlib` library.
- **Dictionary Attack Simulation (`hash_cracker.py`):** Iterates through a structured wordlist to match hashed values, demonstrating how weak credentials can be identified and cracked.

## 📂 Repository Structure
├── hash_tool.py         # Cryptographic hash generator utility
├── hash_cracker.py      # Python dictionary-based hash cracking script
└── README.md            # Project documentation and portfolio overview

## ⚙️ Installation & Usage
1. Run the hash generator: `python3 hash_tool.py`
2. Run the hash cracker script: `python3 hash_cracker.py`

## 💡 Key Takeaways
- Understood how one-way cryptographic hash functions (MD5, SHA-256) protect system passwords.
- Learned the fundamentals of dictionary attacks and how weak passwords expose systems to risk.
- Developed practical Python scripting skills using loops, conditional matching, and the `hashlib` module.
