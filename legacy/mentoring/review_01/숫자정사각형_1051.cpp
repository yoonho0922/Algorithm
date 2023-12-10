#include<iostream>
#include<algorithm>
using namespace std;

int N, M, arr[51][51];

void input() {
	string tmp;
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> tmp;
		for (int j = 0; j < M; j++) {
			arr[i][j] = tmp[j] - '0';
		}
	}
}

int brute() {
	for (int size = min(N, M); size > 1; size--) {
		for (int i = 0; i < N - size + 1; i++) {
			for (int j = 0; j < M - size + 1; j++) {
				int a = arr[i][j];
				int b = arr[i][j + size - 1];
				int c = arr[i + size - 1][j + size - 1];
				int d = arr[i + size - 1][j];

				if (a == b && a == c && a == d)
					return size * size;
			}
		}
	}
	return 1;
}

int main() {
	input();

	cout<<brute();

	return 0;
}