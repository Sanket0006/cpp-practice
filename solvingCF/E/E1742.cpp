#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t; cin >> t;

    for (int i = 0; i < t; i++) {
        int n,q; cin >> n >> q;
        vector<long long> arr(n);
        vector<long long> arrNew(n);
        for (auto &x: arr) cin >> x;
        
        long long Max = arr[0];
        for (int j = 0; j < n; j++) {
            if (arr[j] > Max) Max = arr[j];
            arrNew[j] = Max;
        }
        for (int j = 1; j < n; j++) arr[j] += arr[j-1]; //psum

        //normal print
        for (int j = 0; j < q; j++) {
            int k; cin >> k;
            int idx = upper_bound(arrNew.begin(), arrNew.end(), k) - arrNew.begin();
            if (idx == 0) cout << 0 << " ";
            else cout << arr[idx-1] << " ";
        }
        cout << '\n';
    }
}