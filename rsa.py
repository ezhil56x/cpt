# rsa
import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

class RSA:
    def __init__(self, p=3, q=7):
        self.p = p
        self.q = q
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.e = 7
        self._setE()
        self._setD()

    def encrypt(self, text):
        text = [ord(char) for char in text]
        encrypted = [pow(x, self.e, self.n) for x in text]
        return encrypted

    def decrypt(self, encrypted):
        decrypted = [pow(x, self.d, self.n) for x in encrypted]
        decrypted = [chr(x) for x in decrypted]
        return ''.join(decrypted)

    def getPublicKey(self):
        return self.e, self.n

    def getPrivateKey(self):
        return self.d, self.n

    def _setD(self):
        def gcdExtended(a, b):
            if a == 0:
                return b, 0, 1
            gcd, x1, y1 = gcdExtended(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y

        def modInverse(a, m):
            gcd, x, _ = gcdExtended(a, m)
            if gcd != 1:
                return -1
            return (x % m + m) % m

        self.d = modInverse(self.e, self.phi)

    def _setE(self):
        while self.e < self.phi:
            if gcd(self.e, self.phi) == 1:
                break
            self.e += 1

if __name__ == '__main__':
    p = int(input("Enter a prime number (p): "))
    q = int(input("Enter another prime number (q): "))
    
    encoder = RSA(p, q)
    
    print("Public Key:", encoder.getPublicKey())
    print("Private Key:", encoder.getPrivateKey())
    
    text = input("Enter text to encode: ")
    
    encrypted = encoder.encrypt(text)
    print("Encrypted:", encrypted)
    
    decrypted = encoder.decrypt(encrypted)
    print("Decoded:", decrypted)