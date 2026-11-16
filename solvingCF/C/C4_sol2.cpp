#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    // set<string> registrar;
    map<string, int> registrar;
    int n; cin >> n;

    for (int i = 0; i < n; i++) {
        string name;
        cin >> name;

        if (registrar.count(name) == 0) {
            registrar[name] = 0;
            cout << "OK" << '\n';
        }
        else {
            registrar[name]++;
            cout << name << registrar[name] << '\n';
        }

    }   


}