#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

int main(void) {
    int n;
    cin >> n;
    vector<pair<string, int>> v(n);

    for (auto &p: v){
        cin >> p.first;
        cin >> p.second;
    }

    int mx = 0;
    string bestName;

    for (auto p: v) {
        if (p.second > mx) {
            mx = p.second;
            bestName = p.first;
        }
    }

    cout << bestName << '\n';

}