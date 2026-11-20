#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t; cin >> t;

    for (int i = 0; i < t; i++) {
        int n; cin >> n;
        long long count = 0;
        vector<long long> arr(n);
        map<int, long long> hmap;
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
            hmap[arr[i]-i]++;
        }

        for(const auto &[k,v]: hmap) {
            if (v > 1) {
                count += ((v*(v-1))/2);
            }
        }

        cout << count << '\n';
    }
}