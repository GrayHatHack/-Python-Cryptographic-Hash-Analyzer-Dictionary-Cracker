import hashlib

print("=== Simple Hash Generator & Checker ===")
text = input("Enter a password or text to hash: ")

# MD5 Hash generate karna
md5_hash = hashlib.md5(text.encode()).hexdigest()
print(f"[+] MD5 Hash: {md5_hash}")

# SHA-256 Hash generate karna
sha256_hash = hashlib.sha256(text.encode()).hexdigest()
print(f"[+] SHA-256 Hash: {sha256_hash}")
