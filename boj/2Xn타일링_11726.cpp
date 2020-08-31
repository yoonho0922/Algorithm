#include<iostream>
using namespace std;

int arr[1001];

int dp(int n) {
	if (n == 1)
		return 1;
	else if (n == 2)
		return 2;
	
	if (arr[n] == 0) {
		arr[n] = (dp(n - 1) + dp(n - 2))%10007;
		return arr[n];
	}
	else {
		return arr[n];
	}
}

int main() {
	int n;
	cin >> n;
	cout << dp(n);

	return 0;
}