#include <bits/stdc++.h>
using namespace std;
#define isPositive(x) ((x) > 0)

long long maxSubsquenceSum(vector<int> &v, int n) {
    // 1 2 3 -1 -2
    
    
    long long sum = 0;
    int tMax = v[0];

    for (int i = 1; i < n; i++) {
        if ((isPositive(v[i]) && !isPositive(v[i-1])) || (isPositive(v[i-1]) && (!isPositive(v[i])))) {
            sum += tMax;
            tMax = v[i];
            // cout << i << ", tMax: " << tMax << ", sum: " << sum << '\n';
        }
        else {
            tMax = max(tMax, v[i]);
        }
    }
    sum += tMax;
    return sum;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t; cin >> t;

    for (int i = 0; i < t; i++) {
        int n; cin >> n;
        vector<int> arr(n);

        for (int &x: arr) {
            cin >> x;
        }

    cout << maxSubsquenceSum(arr, n) << '\n';
    }

}