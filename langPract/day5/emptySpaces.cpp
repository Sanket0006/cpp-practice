#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n,m;
    cin >> n >> m;
    int bestRow = -1, bestCount = -1, i = 1;

    vector<string> arr(n);

    for (auto &s: arr) {
        cin >> s;
        int count = 0;
        for (const char c: s) {
            if (c == 'C') count++;
        }
        cout << count << ' ';
        if (count > bestCount) {
            bestCount = count;
            bestRow = i;
        }
        i++;
    }
    cout << "\n" << bestRow << '\n';
    


}