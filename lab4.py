def gcd_extended(a, b):
    """Расширенный алгоритм Евклида для поиска обратного элемента."""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi):
    """Вычисление d (мультипликативно обратного e по модулю phi)."""
    gcd, x, y = gcd_extended(e, phi)
    if gcd != 1:
        raise ValueError("Обратного элемента не существует (e и phi не взаимно просты)")
    else:
        return (x % phi + phi) % phi

# Исходные данные варианта 15
p = 19
q = 23
e = 5
M = 15

# 1. Вычисляем n
n = p * q

# 2. Вычисляем функцию Эйлера
phi = (p - 1) * (q - 1)

# 3. Находим секретную экспоненту d
d = mod_inverse(e, phi)

# 4. Шифрование: C = M^e mod n
C = pow(M, e, n)

# 5. Дешифрование: M_res = C^d mod n
M_res = pow(C, d, n)

print(f"--- Результаты для варианта 15 ---")
print(f"Простые числа: p={p}, q={q}")
print(f"Модуль n: {n}")
print(f"Функция Эйлера phi(n): {phi}")
print(f"Открытая экспонента e: {e}")
print(f"Закрытая экспонента d: {d}")
print(f"--- Процесс ---")
print(f"Исходное сообщение M: {M}")
print(f"Зашифрованное сообщение C: {C}")
print(f"Дешифрованное сообщение: {M_res}")