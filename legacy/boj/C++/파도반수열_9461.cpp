#include<iostream>
using namespace std;

int T, N;
long long P[101];



void dynamic(int N) {
	P[1] = 1, P[2] = 1, P[3] = 1, P[4] = 2, P[5] = 2;

	if (N < 6) {
		cout << P[N];
		return;
	}

	for (int i = 6; i <= N; i++)
		P[i] = P[i - 5] + P[i - 1];

	cout << P[N];
	return;
}

int main() {
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> N;
		dynamic(N);
		cout << '\n';
	}

	return 0;
}