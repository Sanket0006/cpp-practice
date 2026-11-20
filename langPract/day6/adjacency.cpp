#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n, m; cin >> n >> m; // n: nodes; m: edges


    vector<vector<int>> adj(n+1);
    for (int i = 0; i < m; i++) {
        int u,v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int Max = (int) adj[1].size(), node = 1;
    for (int i = 0; i < n+1; i++) {
        if ((int) adj[i].size() > Max) {
            node = i;
            Max = adj[i].size();
        }
    }

    cout << node << " " << Max << '\n';
    sort(adj[node].begin(), adj[node].end());
    for (const int &x: adj[node]) {
        cout << x << " ";
    }
    cout << "\n";
    
}
