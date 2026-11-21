#include <bits/stdc++.h>
using namespace std;


bool isVowel(char x) {
    if (x == 'a' || x == 'e' || x == 'i' || x == 'o'|| x == 'u') return true;
    else return false;
}

int main(void) {
    string word;
    int count = 0; 
    cin >> word;

    for (char c: word) {
        if (isVowel(c)) count++;
    }

    cout << count << '\n';


}