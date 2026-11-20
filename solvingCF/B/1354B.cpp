#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t; cin >> t;

    for (int i = 0; i < t; i++) {
        string str; cin >> str;
        map<char, int> hmap;
        hmap['1'] = 0; hmap['2'] = 0; hmap['3'] = 0;

        int bestLen = 1e9;
        int sz = str.size();
        if (sz < 3) {
            cout << 0 << '\n';
            continue;
        }
        
        int L=0;
        for (int R = 0; R < sz; R++) {
            hmap[str[R]]++;
            while (hmap['1'] >= 1 && hmap['2'] >= 1 && hmap['3'] >= 1) {
                bestLen = min(bestLen, R-L+1);
                hmap[str[L]]--;
                L++;
            }
        }

        if (bestLen == 1e9) bestLen = 0;
        cout << bestLen << '\n';

    }
}