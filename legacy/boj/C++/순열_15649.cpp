#include<iostream>
#include<vector>
using namespace std;

int N, M;
bool visit[9];
vector<int> v;

void go(int cnt) {
	if (cnt == M) {
		for (int i = 0; i < v.size(); i++)
			cout << v[i] << ' ';
		cout << '\n';
		return;
	}
	for (int i = 1; i <= N; i++) {
		if (!visit[i]) {
			visit[i] = true;
			v.push_back(i);
			go(cnt + 1);
			visit[i] = false;
			v.pop_back();
		}
	}
}

int main() {

	cin >> N >> M;
	go(0);
	return 0;
}
