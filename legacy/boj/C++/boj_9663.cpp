#include<iostream>
using namespace std;

int N, total, a[16];

bool promising(int idx) {
	for (int j = 0; j < idx; j++) {
		if (a[j] == a[idx] || abs(a[idx] - a[j]) == (idx - j))
			return false;
	}
	return true;
}

void backtracking(int idx) {
	if (idx == N) {
		total++;
		return;
	}
	for (int i = 0; i < N; i++) {
		a[idx] = i;
		if (promising(idx)) {
			backtracking(idx+1);
		}
	}
}

int main() {
	cin >> N;
	backtracking(0);
	cout << total;
	return 0;
}