#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, q;
    cin >> n;
    vector<int> shopPrices(n);

    for (auto &x: shopPrices) {
        cin >> x;
    }

    cin >> q;    

    sort(shopPrices.begin(), shopPrices.end());

    for (int i = 0 ; i < q ; i++) {
        int x; cin >> x;
        int val = upper_bound(shopPrices.begin(), shopPrices.end(), x) - shopPrices.begin();
        cout << val << '\n';
    }

}