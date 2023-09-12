import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)

    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            break

    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    encrypted = [pow(ord(char), e, n) for char in plaintext]
    return encrypted

def decrypt(private_key, ciphertext):
    d, n = private_key
    decrypted = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(decrypted)

def main():
    bits = 16  # O tamanho dos números primos (ajuste conforme necessário)
    
    print("Gerando chaves...")
    public_key, private_key = generate_keypair(bits)
    print("Chaves geradas.")

    mensagem_original = input("Digite a mensagem a ser cifrada: ")
    mensagem_cifrada = encrypt(public_key, mensagem_original)
    print("Mensagem cifrada:", mensagem_cifrada)

    mensagem_decifrada = decrypt(private_key, mensagem_cifrada)
    print("Mensagem decifrada:", mensagem_decifrada)

if __name__ == "__main__":
    main()