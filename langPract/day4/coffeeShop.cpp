#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n; cin >> n;
    queue<string> q;

    for (int i = 0; i < n; i++) {
        string type;
        cin >> type;
        if (type == "join") {
            string name;
            cin >> name;
            q.push(name);
        }
        else if (type == "count") {
            cout << q.size() << '\n';
        }
        else {
            cout << q.front() << '\n';
            q.pop();
        }
    }

}