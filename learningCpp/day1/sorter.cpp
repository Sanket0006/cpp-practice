#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <string>
using namespace std;

int main(void) {
    int n;
    cin >> n;

    vector<pair<int, string>> arr(n);

    for (auto &p: arr) {
        cin >> p.second >> p.first;
    }

    sort(arr.begin(), arr.end());

    for (auto p: arr) {
        cout << p.second << " " << p.first << '\n';
    }
}