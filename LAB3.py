import struct

def rol(val, r_bits, max_bits=32):
    """Циклический сдвиг влево."""
    return ((val << (r_bits % max_bits)) & (2**max_bits - 1)) | \
           ((val & (2**max_bits - 1)) >> (max_bits - (r_bits % max_bits)))

def ror(val, r_bits, max_bits=32):
    """Циклический сдвиг вправо."""
    return ((val & (2**max_bits - 1)) >> (r_bits % max_bits)) | \
           (val << (max_bits - (r_bits % max_bits)) & (2**max_bits - 1))

class FeistelNetwork:
    def __init__(self, key_64bit, rounds=24):
        self.rounds = rounds
        # Разделяем 64-битный ключ на две 32-битные части K1 и K2
        self.k1 = (key_64bit >> 32) & 0xFFFFFFFF
        self.k2 = key_64bit & 0xFFFFFFFF

    def get_round_key(self, i):
        """Вычисление параметра Vi: K1 ROL i XOR K2 ROR i"""
        return rol(self.k1, i) ^ ror(self.k2, i)

    def f_function(self, x1_prev, v_i):
        """Образующая функция для 15 варианта (XOR)"""
        return x1_prev ^ v_i

    def encrypt_block(self, block_128bit):
        # Разбиваем 128 бит на 4 ветви по 32 бита
        x = list(struct.unpack('>4I', block_128bit))
        
        for i in range(1, self.rounds + 1):
            v_i = self.get_round_key(i)
            f_i = self.f_function(x[0], v_i)
            
            # Применяем формулы из методички
            new_x1 = x[1] ^ f_i
            new_x2 = x[2]
            new_x3 = x[3]
            new_x4 = x[0]
            x = [new_x1, new_x2, new_x3, new_x4]
            
        return struct.pack('>4I', *x)

    def decrypt_block(self, block_128bit):
        x = list(struct.unpack('>4I', block_128bit))
        
        # Дешифрование идет в обратном порядке
        for i in range(self.rounds, 0, -1):
            v_i = self.get_round_key(i)
            
            # Инвертируем шаги раунда
            old_x0 = x[3]
            f_i = self.f_function(old_x0, v_i)
            old_x1 = x[0] ^ f_i
            old_x2 = x[1]
            old_x3 = x[2]
            x = [old_x0, old_x1, old_x2, old_x3]
            
        return struct.pack('>4I', *x)

# Демонстрация работы
key = 0x0123456789ABCDEF
cipher = FeistelNetwork(key)

text = "Hello Feistel123" # 16 байт = 128 бит
data = text.encode('utf-8')

encrypted = cipher.encrypt_block(data)
decrypted = cipher.decrypt_block(encrypted)

print(f"Исходный текст: {text}")
print(f"Шифрограмма (hex): {encrypted.hex()}")
print(f"Дешифрованный текст: {decrypted.decode('utf-8')}")