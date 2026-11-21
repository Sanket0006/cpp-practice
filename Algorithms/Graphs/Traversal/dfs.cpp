#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> adj;
vector<int> seen;
map<int,int> Count;


void dfs(int u, int group) {
    seen[u] = group;
    Count[group]++;
    for (int v: adj[u]) {
        if (seen[v] == 0) {
            dfs(v, group);
        }
    }
}



int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, m; cin >> n >> m;
    adj.assign(n+1, {});
    seen.assign(n+1, false);

    for (int i = 0; i < m; i++) {
        int u,v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int group = 0;
    for (int i = 1; i < n+1; i++) {
        if (seen[i] == 0) {
            dfs(i, ++group); 
        }

    }



    int Max = 0;
    for (const auto &[k,v]: Count) {
        if (v > Max) Max = v;
    }

    cout << group << " " << Max << '\n';

}