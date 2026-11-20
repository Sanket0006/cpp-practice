#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n,m; cin >> n >> m;
    vector<vector<int>> adj(n+1);

    for (int i = 0; i < m; i++) {
        int u,v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    
    int s = 1;
    vector<int> dist(n+1, -1);
    dist[s] = 0;

    queue<int> q;
    q.push(s);

    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (const int &v: adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }

    for (int i = 1; i < n+1; i++) {
        cout << dist[i] << ' ';
    }
    cout << '\n';


}