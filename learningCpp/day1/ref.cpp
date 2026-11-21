#include <iostream>
#include <vector>
using namespace std;

int main(void) {
    int n;
    cin >> n;
    vector<int> arr(n);

    for (int &x: arr) {
        cin >> x;
        x *= 2;
    }

    for (int x: arr) {
        cout << x << ' ';
    }
    cout << '\n';
}
