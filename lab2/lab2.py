from sympy import randprime, gcd, primerange
from random import choice
import random

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None
    return x % m

def generate_two_simple():
    p = randprime(1, 1000)  
    q = randprime(1, 1000)
    while p == q:
        q = randprime(1, 1000)
    return p, q

# Генерация ключей
p, q = generate_two_simple()
N = p * q
phi = (p - 1) * (q - 1)

# Выбор e
primes = list(primerange(2, phi))
e = choice(primes)
while gcd(e, phi) != 1:
    e = choice(primes)

# Вычисление d
d = modinv(e, phi)

print(f'p = {p}, q = {q}')
print(f'N = {N}')
print(f'φ = {phi}')
print(f'e = {e}')
print(f'd = {d}')
print(f'open_key = ({e}, {N})')
print(f'private_key = ({d}, {N})')

# Шифрование
word = list(input("Введите сообщение: "))
word = [ord(elem) for elem in word]
print(f"Исходное (числа): {word}")

encrypted = []
for elem in word:
    encrypted.append(pow(elem, e, N))

print(f"Зашифрованное: {encrypted}")

# Расшифровка
decrypted = []
for elem in encrypted:
    decrypted.append(pow(elem, d, N))

print(f"Расшифрованное: {decrypted}")
print(f"Текст: {''.join([chr(x) for x in decrypted])}")