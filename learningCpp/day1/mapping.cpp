#include <iostream>
#include <map>
#include <string>
using namespace std;


int main(void) {
    map<string, int> hmap;

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        hmap[s]++;
    }

    string query;
    cin >> query;

    cout << hmap[query] << '\n';
}
