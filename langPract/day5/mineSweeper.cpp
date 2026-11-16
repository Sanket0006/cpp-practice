#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n,m;
    cin >> n >> m;

    vector<string> grid(n);

    for (string &s: grid) {
        cin >> s;
    }

    // int dr[] = {-1,1,0,0};
    // int dc[] = {0,0,-1,1};
    int dr[] = {-1,1,0,0,-1,-1,1,1};
    int dc[] = {0,0,-1,1,1,-1,-1,1};
    int sz = 8;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            char curr = grid[i][j];
            if (curr == '*') {cout << '*'; continue;}
            int count = 0;
            for (int k = 0; k < sz; k++) {
                int nr = i + dr[k], nc = j + dc[k];
                if (nr < 0 || nc < 0 || nr >= n || nc >= m) continue;
                if (grid[nr][nc] == '*') count++;
                
            }
            cout << count;
        }
        cout << '\n';
    }

}