#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n; cin >> n;
    vector<int> arr(n);

    for(int &x: arr) {
        cin >> x;
    }

    long long sum = 0;
    priority_queue<int, vector<int>, greater<int>> pq;

    for (int i = 0; i < n; i++) {
        sum += arr[i];
        pq.push(arr[i]);
        if (sum < 0) {
            sum -= pq.top();
            pq.pop();
        }
    }


    cout << pq.size() << '\n';

}