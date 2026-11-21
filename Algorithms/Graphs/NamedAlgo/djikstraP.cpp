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

    int s = 1;

    priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<pair<long long,int>>> pq;
    vector<long long> dist(n+1, LLONG_MAX);
    dist[s] = 0; pq.push({0, s});

    while (!pq.empty()) {

        auto [d,u] = pq.top(); pq.pop();

        if (d > dist[u]) continue;

        for (auto &[v, w]: adj[u]) {

            if (w + d < dist[v]) {
                dist[v] = w + d;
                pq.push({dist[v], v});
            }

        }


    }

}