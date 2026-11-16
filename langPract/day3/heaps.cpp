#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    priority_queue<int> pq;

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        string todo;
        cin >> todo;
        if (todo == "add") {
            int x;
            cin >> x;
            pq.push(x);
        }
        else {
            int k  = pq.top();
            pq.pop();
            cout << k << '\n';
        }
    }
}