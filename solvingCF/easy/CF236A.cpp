#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string inp;
    cin >> inp;
    set<char> s;

    for (char &c: inp) {
        s.insert(c);
    }
    if (s.size() % 2 == 0) {
        cout << "CHAT WITH HER!" << '\n';
    }
    else {
        cout << "IGNORE HIM!" << '\n';
    }

}