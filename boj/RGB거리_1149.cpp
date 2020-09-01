#include<iostream>
#include<algorithm>
using namespace std;

int N, res, price[1001][3], D[1001][3];

void input() {
	cin >> N;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < 3; j++)
			cin >> price[i][j];
}

void dynamic() {
	for (int i = 0; i < 3; i++)
		D[0][i] = price[0][i];

	for (int i = 1; i < N; i++) {
		D[i][0] = min(D[i - 1][1], D[i - 1][2]) + price[i][0];
		D[i][1] = min(D[i - 1][0], D[i - 1][2]) + price[i][1];
		D[i][2] = min(D[i - 1][0], D[i - 1][1]) + price[i][2];
	}
}

int main() {
	input();
	dynamic();

	res = 999999;
	for (int i = 0; i < 3; i++)
		if (D[N - 1][i] < res)
			res = D[N - 1][i];

	cout << res;
	return 0;
}