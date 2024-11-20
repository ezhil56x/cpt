# caesar
def encrypt(message, key):
    encrypted = ""
    for char in message:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift + key) % 26 + shift)
        else:
            encrypted += char
    return encrypted

def decrypt(message, key):
    return encrypt(message, -key)

def main():
    message = "Hello, World!"
    key = 3
    encrypted = encrypt(message, key)
    print(encrypted)
    decrypted = decrypt(encrypted, key)
    print(decrypted)

if __name__ == "__main__":
    main()