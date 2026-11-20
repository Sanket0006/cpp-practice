#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t; cin >> t;

    for (int i = 0; i < t; i++) {
        int n; cin >> n;
        vector<int> hmap(n+1);
        int best = 0;
        for (int j = 0; j < n; j++) {
            int k; cin >> k;
            hmap[k]++;
        }

        for (int s = 2; s <= 2*n; s++) {
            int teams = 0;
            for (int w = 1; w <= n; w++) {

                if (s-w <= n && w < s - w) {
                    teams += min(hmap[w], hmap[s-w]);
                }
                else if (w == s - w) {
                    teams += hmap[w] / 2;
                }
                best = max(best, teams);
            }
        }
        cout << best << '\n';

    }

}