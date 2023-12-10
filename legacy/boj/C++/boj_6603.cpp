#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;

int S[100][14], M = 6;
bool visit[50];

void input() {
	int k, i=0;
	do {
		cin >> k;
		S[i][0] = k;
		for (int j = 1; j <= k; j++)
			cin >> S[i][j];
		i++;
	} while (k != 0);
}

void go(int i, int idx, int cnt) {

	if (cnt == M) {
		for (int j = 1; j <= S[i][0]; j++) {
			if (visit[j])
				cout << S[i][j] << " ";
		}
		cout << '\n';
		return;
	}


	for (int j = idx; j <= S[i][0]; j++) {
		if (!visit[j]) {
			visit[j] = true;
			go(i ,j, cnt + 1);
			visit[j] = false;
		}
	}
}

void print_fnc(int n) {
	cout << n << " ";
}

int main() {
	input();

	int i = 0;

	while (S[i][0] != 0) {
		go(i, 1, 0);
		memset(visit, 0, 50);
		cout << '\n';
		i++;
	}

	return 0;
}