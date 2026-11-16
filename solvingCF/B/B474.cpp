#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n; cin >> n;
    vector<int> psum(n+1);
    for (int i = 1; i < n+1; i++) {
        int temp; cin >> temp;
        psum[i] = psum[i-1] + temp;
    }

    int m; cin >> m;

    for (int i = 0; i < m; i++) {
        int curr; cin >> curr;
        int pile = lower_bound(psum.begin(), psum.end(), curr) - psum.begin();
        cout << pile << '\n';
    }

}