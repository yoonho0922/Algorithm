#include<iostream>
using namespace std;

int D[1000001];

int dp(unsigned long long n) {
	if (n == 1)
		return 1;
	else if (n == 2)
		return 2;

	if (D[n] == 0) {
		D[n] = (dp(n-1) + dp(n-2)) % 15746;
		return D[n];
	}
	else {
		return D[n];
	}
}

int main() {
	unsigned long long n;
	cin >> n;
	cout << dp(n);

	return 0;
}