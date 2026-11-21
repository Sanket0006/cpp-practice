#include <iostream>
#include <climits>
#include <algorithm>
using namespace std;

int main(void) {

    int n;
    cin >> n;

    int mx = INT_MIN;
    int mn = INT_MAX;
    int sum = 0;

    for (int i = 0; i<n; i++) {
        int t;
        cin >> t;
        mx = max(mx, t);
        mn = min(mn, t);
        sum += t;

    }

    cout << mn << "\n" << mx << "\n";

}