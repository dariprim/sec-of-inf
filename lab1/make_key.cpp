#include <iostream>
#include <fstream>
using namespace std;

int main() {
    unsigned char key[256];
    
    // "перевёртыш" ключ для простоты
    // Байт 0 заменяется на 255, 1 на 254
    for (int i = 0; i < 256; i++) {
        key[i] = 255 - i;
    }
    
    // Сохраняем в файл
    ofstream out("key.txt", ios::binary);
    out.write((char*)key, 256);
    out.close();
    
    cout << "Ключ создан и сохранён в key.txt" << endl;
    cout << "Правило замены: байт N -> байт (255-N)" << endl;
    
    return 0;
}