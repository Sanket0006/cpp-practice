#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    priority_queue<pair<int, string>, vector<pair<int, string>>, greater<>> pq;

    for (int i = 0; i < n; i++) {
        string type;
        cin >> type;
        if (type == "send") {
            string docName;
            int priority;
            cin >> docName >> priority;
            pq.push({priority, docName});
        }
        else {
            auto top = pq.top();
            cout << top.second << '\n';
            pq.pop();
        }
    }
}