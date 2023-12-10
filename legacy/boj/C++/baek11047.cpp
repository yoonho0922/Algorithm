#include<iostream>
using namespace std;

int value[11];
int N, K, res = 0;

int main() {

	cin >> N >> K;

	for (int i = 0; i < N; i++) {
		cin >> value[i];
	}

	for (int i = 0; i < N; i++) {
		res += K / value[N - 1 - i];
		K = K % value[N - 1 - i];
	}

	cout << res;
}