#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int N, M, arr[51][51], check[10];

void input() {
	string s;
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> s;
		for (int j = 0; j < M; j++) {
			arr[i][j] = s[j] - '0';
		}
	}
}

int brute() {
	int size = min(N, M);
	while (size > 1) {
		for (int i = 0; i <= N - size; i++) {
			for (int j = 0; j <= M - size; j++) {
				int a = arr[i][j];
				int b = arr[i][j + size - 1];
				int c = arr[i + size - 1][j + size - 1];
				int d = arr[i + size - 1][j];
				if (a == b && a == c && a == d)
					return size*size;
			}
		}
		size--;
	}
	return 1;
}

int main() {
	input();
	cout << brute();

	return 0;
}