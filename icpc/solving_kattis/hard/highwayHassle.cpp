#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int test; cin >> test;

    for (int i = 0; i < test; i++) {

        int n,m,s; cin >> n >> m >> s; // nodes, edges, petrol pump
        int fuel; cin >> fuel;

        vector<int> pumps(n+1, -1);
        vector<long long> cost(n+1, 1e9);
        vector<vector<pair<int,int>>> adj(n);
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
        
        for (int j = 0; j < m; j++) {
            int u, v, cof; cin >> u >> v >> cof;
            adj[u].push_back({v, cof});
            adj[v].push_back({u, cof});
        }
        for (int j = 0; j < s; j++) {
            int node, cost; cin >> node >> cost;
            pumps[node] = cost;
        }

        int src, dst; cin >> src >> dst; 

        cost[src] = 0;
        pq.push({0, src});

        while (!pq.empty()) {
            auto [u, cof] = pq.top(); pq.pop();

            if (cof < cost[u]) continue;

            for (auto &[v, fuelNeed]: adj[u]) {
                if (fuelNeed > fuel) continue;

                if (fuelNeed * pumps[u] + cof < cost[u]) {
                    cost[v] = fuelNeed * pumps[u] + cof;
                    pq.push({cost[v], v});
                }
            }

        }

        for (auto x: cost) {
            cout << x << " ";
        }
        cout << '\n';


    }


}