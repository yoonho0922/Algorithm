#include<iostream>
#include<cstring>
using namespace std;

int N, K, coin[101], D[10001];

void input() {
	cin >> N >> K;
	for (int i = 0; i < N; i++)
		cin >> coin[i];
}

void dynamic() {
	for (int i = 0; i < N; i++) {
		for (int j = coin[i]; j <= K; j++) {
			D[j] += + D[j - coin[i]];
		}
	}
}

int main() {
	input();
	D[0] = 1;
	dynamic();
	cout << D[K];
	return 0;
}