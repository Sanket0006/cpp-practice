#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    vector<pair<string,int>> arr(n);

    for (auto &p: arr) {
        cin >> p.first >> p.second; 
    }

    sort(arr.begin(), arr.end(), [](const auto &x, const auto &y) {
        if (x.second != y.second) return x.second > y.second;
        return x.first < y.first;
    });

    for (auto &p: arr) {
        cout << p.first << " " << p.second << '\n';
    }

}