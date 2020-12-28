#include<iostream>
using namespace std;

int N, res, tri[501][501], D[501][501];

void input() {
	cin >> N;
	for (int i = 0; i < N; i++)
		for (int j = 0; j <= i; j++)
			cin >> tri[i][j];
}

int D_max(int i, int j) {
	int left = D[i - 1][j - 1];
	int right = D[i - 1][j];
	if (left > right)
		return left;
	else
		return right;
}

void dynamic() {
	
	for (int i = 0; i < N; i++) {
		for (int j = 0; j <= i; j++) {
			if (j == 0) {	// 哭率 场老 版快
				D[i][j] = D[i - 1][0] + tri[i][j];
			}
			else if (j == i) {	// 坷弗率 场老 版快
				D[i][j] = D[i - 1][i - 1] + tri[i][j];
			}
			else {
				D[i][j] = D_max(i, j) + tri[i][j];
			}
		}
	}
}

int main() {
	input();
	dynamic();

	for (int i = 0; i < N; i++)
		if (D[N - 1][i] > res)
			res = D[N - 1][i];
	
	cout << res;

	return 0;
}