#include <bits/stdc++.h>
using namespace std;

bool isValid(vector<string> &grid, int n, int m) {
    int dr[] = {-1,1,0,0,-1,-1,1,1};
    int dc[] = {0,0,-1,1,1,-1,-1,1};

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == '*') continue;; //TODO
            int cnt = 0;
            for (int k = 0; k < 8; k++) {
                int nr = i + dr[k], nc = j + dc[k];
                if (nr < 0 || nc < 0 || nr >= n || nc >= m) continue;
                if (grid[nr][nc] == '*') cnt++;
            }
            if (cnt == 0 && grid[i][j] == '.') continue;
            else if (cnt > 0 && grid[i][j] == '.') return false;
            else if (grid[i][j] - '0' != cnt) return false;
        }
    }
    return true;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n,m; cin >> n >> m;

    vector<string> grid(n);
    for (auto &p: grid) cin >> p;

    if (isValid(grid, n, m)) cout << "YES" << '\n';
    else cout << "NO" << '\n';


}