# elgamal
import sympy
import random
from binascii import hexlify, unhexlify

def mod_inverse(a, p):
    t, new_t = 0, 1
    r, new_r = p, a

    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r

    if r > 1:
        raise ValueError(f"{a} has no inverse mod {p}")

    if t < 0:
        t = t + p
    return t

def shared_secret(g, x, p):
    return pow(g, x, p)

def elgamal_key_generation(p, g):
    x = random.randint(1, p-2)  # Private key
    y = shared_secret(g, x, p)  # Public key
    print(f"Private key (x): {x}")


    print(f"Public key (y): {y}")
    return (p, g, y), x

def encrypt(m, r, g, p, h):
    c1 = pow(g, r, p)
    c2 = (m * pow(h, r, p)) % p
    print(f"Random value (r): {r}")
    print(f"Ciphertext (c1, c2): ({c1}, {c2})")
    return c1, c2

def decrypt(x, c1, c2, p):
    s = pow(c1, x, p)
    s_inv = mod_inverse(s, p)
    m = (c2 * s_inv) % p
    print(f"Shared secret (s): {s}")
    print(f"Modular inverse of shared secret (s_inv): {s_inv}")
    return m

print("ElGamal Algorithm")
input_message = input("Enter the message to be encrypted: ")
input_bytes = str.encode(input_message)
m = int(hexlify(input_bytes), 16)
p = sympy.randprime(m*2, m*4)
g = sympy.randprime(int(m/2), m)
print(f"Prime number (p): {p}")
print(f"Generator (g): {g}")
print("\n")

# Key generation
print("Key Generation")
public_key, private_key = elgamal_key_generation(p, g)
print(f"(p, g, h): {public_key}")
print("\n")

# Encryption
print("Encryption")
print(f"Original message: {input_message}")
r = random.randint(1, p-2)
encrypted = encrypt(m, r, public_key[1], public_key[0],
                    public_key[2])
print("\n")

# Decryption
print("Decryption")
decrypted_int = decrypt(private_key, encrypted[0], encrypted[1], p)
decrypted_hex = format(decrypted_int, 'x')
decrypted_message = unhexlify(decrypted_hex)
print(f"Decrypted Message: {decrypted_message.decode()}")