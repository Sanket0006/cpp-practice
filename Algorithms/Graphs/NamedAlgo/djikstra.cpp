#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n,m; cin >> n >> m;
    vector<vector<pair<int,int>>> adj(n+1);
    for (int i = 0; i < m; i++) {
        int u,v,w; cin >> u >> v >> w;
        adj[u].push_back({v,w});
        adj[v].push_back({u,w});
    }

    int s = 0;
    // Pair A,B: distance, Node
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>()> pq;
    vector<int> dist(n+1, 1e9);
    dist[s] = 0; pq.push({0, 1});

    while (!pq.empty()) {

        auto [d,u] = pq.top(); pq.pop();

        if (d > dist[u]) continue;

        for (auto &[v,w]: adj[u]) {

            if (d + w < dist[v]) {
                dist[v] = d + w;
                pq.push({dist[v], v});
            }

        }

    }


    
}