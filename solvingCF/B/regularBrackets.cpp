#include <bits/stdc++.h>
using namespace std;

int regularHowMuch(string parenthisis) {
    stack<char> stck;
    int k = 0;
    for (char c: parenthisis) {
        if ((c == '}' || c == ']' || c == ')') && (!stck.empty())){
            char tp = stck.top();
            if (c == ')' && tp == '(') {stck.pop(); k++;}
            else {stck.pop();}
        }
        else {stck.push(c);}
    }
    return k*2;
}

int main(void) {
    //TODO
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s;
    cin >> s;

    cout << regularHowMuch(s) << '\n';
}