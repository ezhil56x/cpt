# diffie
import random

def diffie_hellman_key_exchange(p, g):
    a = random.randint(1, p - 2)  # Private key for party A
    b = random.randint(1, p - 2)  # Private key for party B
    A = pow(g, a, p)
    B = pow(g, b, p)
    secret_key_A = pow(B, a, p)
    secret_key_B = pow(A, b, p)
    assert secret_key_A == secret_key_B
    return secret_key_A

if __name__ == "__main__":
  print("Diffie-Hellman (DH) Key Exchange")
  
  p = int(input("Enter a prime number (p): "))
  g = int(input("Enter a base (g): "))
  
  shared_secret = diffie_hellman_key_exchange(p, g)
  
  print(f"Shared Secret Key: {shared_secret}")
