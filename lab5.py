import hashlib

def generate_keys(p, q, e):
    """Генерация параметров ключей RSA."""
    n = p * q
    phi = (p - 1) * (q - 1)
    # Вычисление секретного ключа d (обратное e по модулю phi)
    d = pow(e, -1, phi)
    return (e, n), (d, n)

def get_hash(message):
    """Преобразование текста в число (хэш-сумма)."""
    hash_object = hashlib.sha256(message.encode())
    # Берем числовое представление хэша для работы с RSA
    return int(hash_object.hexdigest(), 16) % 1000 # Для упрощения примера берем остаток

def sign_message(message, private_key):
    """Создание подписи: S = Hash(M)^d mod n"""
    d, n = private_key
    h = get_hash(message)
    signature = pow(h, d, n)
    return signature

def verify_signature(message, signature, public_key):
    """Проверка подписи: Hash(M) == S^e mod n"""
    e, n = public_key
    h = get_hash(message)
    decrypted_hash = pow(signature, e, n)
    return h == decrypted_hash

# Исходные данные
p = 61
q = 53
e = 17 # Открытая экспонента

# 1. Генерация ключей
public_k, private_k = generate_keys(p, q, e)
print(f"Открытый ключ (e, n): {public_k}")
print(f"Секретный ключ (d, n): {private_k}")

# 2. Подписание сообщения
msg = "хочется тепл"
sig = sign_message(msg, private_k)
print(f"Сообщение: {msg}")
print(f"Подпись (S): {sig}")

# 3. Проверка
is_valid = verify_signature(msg, sig, public_k)
print(f"Подпись верна: {is_valid}")