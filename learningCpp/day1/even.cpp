#include <iostream>
#include <vector>
using namespace std;

int main(void) {
    int n = 0;
    cin >> n;
    vector<int> v(n);

    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }
    
    for (int x: v) {
        if (x % 2 == 0) cout << x << " ";
    }
    cout << '\n';


}