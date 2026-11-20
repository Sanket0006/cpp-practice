#include <bits/stdc++.h>
using namespace std;

int queryCheck(vector<int> &arr, int k) {
    int check = lower_bound(arr.begin(), arr.end(), k) - arr.begin();
    if (check == (int) arr.size()) return -1;
    return check + 1;
}



int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t; cin >> t;

    for (int i = 0; i < t; i++) {
        int n,q; cin >> n >> q;
        vector<int> arr(n);
        for (int &x: arr) cin >> x;
        sort(arr.begin(), arr.end(), greater<int>());

        for(int j = 1; j < n; j++) {
            arr[j] += arr[j-1];
        }

        for (int j = 0; j < q; j++) {
            int k; cin >> k;
            cout << queryCheck(arr, k) << '\n';
        }
    }


}