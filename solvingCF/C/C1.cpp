#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n; cin >> n;
    vector<int> arr(n);

    for(int &x: arr) {
        cin >> x;
    }

    int best = 0, L = 0, R = 0;
    int sum = 0;
    while (L < n || R < n) {
        if (sum >= 0) sum += arr[++R];
        else sum -= arr[L++];
        best = max(best, R-L+1);
    }

    cout << best << '\n';

}