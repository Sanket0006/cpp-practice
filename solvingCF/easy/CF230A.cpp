#include <bits/stdc++.h>
using namespace std;

int canDefeat(vector<pair<int,int>> &arr, int s){ 
    for (auto &p: arr) {
        if (s <= p.first) {
            return false;
        }
        s += p.second;
    }
    return true;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int s, n; cin >> s >> n;
    vector<pair<int,int>> arr(n);

    for (auto &p: arr) {
        cin >> p.first >> p.second;
    }

    sort(arr.begin(), arr.end());

    if (canDefeat(arr, s)) cout << "YES" << '\n';
    else cout << "NO" << '\n';




}