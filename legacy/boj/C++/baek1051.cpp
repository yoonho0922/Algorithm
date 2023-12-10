//¹Ì¿Ï¼º
#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

int main() {
	int N, M, tmp, max, res = 1;
	int a, b, c, d;	// vertex
	cin >> N>>M;

	int** matrix = new int* [N];
	for (int i = 0; i < N; i++) 
		matrix[i] = new int[M];

	for (int i = 0; i < N; i++) {	//init matrix
		cin >> tmp;
		for (int j = 0; j < M; j++) {
			matrix[i][j] = tmp/ (int)pow(10, M - j - 1) % 10;
		}
	}

	if (N < M)	// get max
		max = M;
	else
		max = N;

	for (int i = 2; i <= max; i++) { // i : rectangle size
		for (int j = 0; j <= N - i; j++) {
			for (int k = 0; k <= M - i; k++) {
				a = matrix[j][k];
				b = matrix[j][k + i - 1];
				c = matrix[j + i - 1][k];
				d = matrix[j + i - 1][k + i - 1];
				if (a == b && b == c && c == d)
					res = i*i;
			}
		}
	}

	cout << res;

	return 0;
}