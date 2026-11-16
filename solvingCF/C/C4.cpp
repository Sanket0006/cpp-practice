#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    set<string> registrar;
    int n; cin >> n;

    for (int i = 0; i < n; i++) {
        string name;
        cin >> name;

        if (registrar.count(name) == 1) {
            int i = 1;
            while (registrar.count(name + to_string(i)) != 0) i++;
            cout << name + to_string(i) << '\n';
            registrar.insert(name + to_string(i));
        }
        else {
            registrar.insert(name);
            cout << "OK" << '\n';
        }
    }


}