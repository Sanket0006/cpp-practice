#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n; cin >> n;

    if (n == 1) {
        int k; cin >> k;
        cout << k << '\n';
    }
    int sum = 0;
 
    for (int i = 0; i < n; i++) {
        int k; cin >> k;
        if (i == 1) {sum -= k; continue;}
        sum += abs(k);
    }

    cout << sum << '\n';


}