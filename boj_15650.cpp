#include<iostream>
#include<vector>
using namespace std;

int N, M;
bool visit[9];
vector<int> v;

void go(int idx, int cnt) {

	if (cnt == M) {
		for (int i = 1; i <= N; i++) {
			if (visit[i])
				cout << i << " ";
		}
		cout << '\n';
		return;
	}
	for (int i = idx; i <= N; i++) {
		if (!visit[i]) {
			visit[i] = true;
			go(i, cnt + 1);
			visit[i] = false;
		}
	}
}

int main() {
	cin >> N >> M;

	go(1, 0);
	return 0;
}