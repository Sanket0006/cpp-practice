#include <iostream>
#include <string>
using namespace std;

int main(void) {
    int age;
    string name;

    cout << "Input:\n";
    cin >> age >> ws;
    getline(cin, name);
    
    cout << "\nOutput:\n";
    cout << name << " is " << age << "\n";

}