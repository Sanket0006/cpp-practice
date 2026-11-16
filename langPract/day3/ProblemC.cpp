#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    vector<int> arr(n);

    for (int &e: arr) {
        cin >> e;
    }

    int m;
    cin >> m;
    
    sort(arr.begin(), arr.end());

    for (int i = 0; i < m; i++) {
        int inp;
        cin >> inp;
        int k = upper_bound(arr.begin(), arr.end(), inp) - arr.begin();
        cout << k << '\n';
    }

    

}