#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    map<string, int> tokens;

    int n;
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        string word;
        cin >> word;
        tokens[word]++;
    }

    for(const auto &[key, value]: tokens) {
        cout << key << " " << value << '\n';
    }

}