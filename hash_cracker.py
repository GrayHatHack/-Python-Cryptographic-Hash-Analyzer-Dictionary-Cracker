import hashlib

print("=== Simple Python Hash Cracker ===")

# Maan lijiye humare paas yeh target MD5 hash hai (yeh 'password123' ka hash hai)
target_hash = "482c811da5d5b4bc6d497ffa98491e38"

# Ek choti si sample wordlist (Common passwords)
wordlist = ["admin", "123456", "password", "secret", "password123", "kali123"]

print(f"[*] Target Hash to crack: {target_hash}\n")

found = False
for word in wordlist:
    # Har word ka MD5 hash banakar target hash se match karenge
    hashed_word = hashlib.md5(word.encode()).hexdigest()
    print(f"[-] Trying password: {word} --> Hash: {hashed_word}")
    
    if hashed_word == target_hash:
        print(f"\n[+] SUCCESS! Password found: {word}")
        found = True
        break

if not found:
    print("\n[-] Password not found in the wordlist.")
