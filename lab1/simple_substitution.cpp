#include <iostream>
#include <fstream>
using namespace std;

int main() {
    string input_file, output_file, key_file;
    char mode;
    
    cout << "Шифровать (e) или расшифровать (d)? ";
    cin >> mode;
    cout << "Введите имя входного файла: ";
    cin >> input_file;
    cout << "Введите имя выходного файла: ";
    cin >> output_file;
    cout << "Введите имя файла с ключом: ";
    cin >> key_file;
    
    // 1. Открываем файл с ключом
    ifstream key_stream(key_file, ios::binary);
    if (!key_stream) {
        cout << "Ошибка: не могу открыть файл с ключом!" << endl;
        return 1;
    }
    
    // 2. Читаем ключ 
    unsigned char key[256];
    key_stream.read((char*)key, 256);
    key_stream.close();
    
    // 3. Открываем входной и выходной файлы
    ifstream in(input_file, ios::binary);
    ofstream out(output_file, ios::binary);
    
    if (!in || !out) {
        cout << "Ошибка открытия файлов!" << endl;
        return 1;
    }
    
    // 4. Обрабатываем каждый байт
    unsigned char byte;
    while (in.read((char*)&byte, 1)) {
        unsigned char result;
        
        if (mode == 'e' || mode == 'E') {
            // ШИФРОВАНИЕ
            result = key[byte];
        } else {
            // РАСШИФРОВАНИЕ
            result = 0;
            for (int i = 0; i < 256; i++) {
                if (key[i] == byte) {
                    result = i;
                    break;
                }
            }
        }
        
        out.write((char*)&result, 1);
    }
    
    in.close();
    out.close();
    cout << "Готово!" << endl;
    
    return 0;
}