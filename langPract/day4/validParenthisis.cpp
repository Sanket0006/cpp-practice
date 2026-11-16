#include <bits/stdc++.h>
using namespace std;

bool isValid(string parenthisis) {
    stack<char> stck;

    for (char c: parenthisis) {
        if ((c == '}' || c == ']' || c == ')') && (!stck.empty())){
            char tp = stck.top();
            if (c == '}' && tp == '{') stck.pop();
            else if (c == ']' && tp == '[') stck.pop();
            else if (c == ')' && tp == '(') stck.pop();
            else return false;
        }
        else stck.push(c);
    }
    if (stck.size() > 0) return false;
    else {
        return true;
    }
}

int main(void) {
    //TODO
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;

        if (isValid(s)) cout << "YES" << '\n';
        else cout << "NO" << '\n';
    }
}