#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>

using namespace std;

int main()
{
    string filename;
    cout << "Введите имя файла";
    cin >> filename;

    ifstream file(filename, ios::binary);
    if (!file){
        cout << "Ошибка чтения" << endl;
        return 1;
    }

    vector <long long> count(256, 0);
    unsigned char byte;
    long long total = 0;

    while (file.read((char*)&byte, 1)) {
        count[byte]++;
        total++;
    }
    file.close();

    // Выводим относительные частоты
    cout << "Байт | Частота | Относительная частота" << endl;
    cout << "--------------------------------------" << endl;
    for (int i = 0; i < 256; i++) {
        if (count[i] > 0) {
            double relative = (double)count[i] / total * 100;
            cout << setw(4) << i << " | " 
                 << setw(7) << count[i] << " | " 
                 << fixed << setprecision(4) << relative << "%" << endl;
        }
    }
    
    return 0;
}