#include <iostream>
#include <fstream>
using namespace std;

int main() {
    string filename;
    cout << "Введите имя файла: ";
    cin >> filename;
    
    ifstream file(filename, ios::binary | ios::ate);
    if (!file) {
        cout << "Ошибка открытия файла!" << endl;
        return 1;
    }
    
    streamsize size = file.tellg();
    cout << "Длина файла в байтах: " << size << endl;
    file.close();
    
    return 0;
}