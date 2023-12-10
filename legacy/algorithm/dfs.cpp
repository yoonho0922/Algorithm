// DFS
// input
// 5 5 3
// 5 4
// 5 2
// 1 2
// 3 4
// 3 1
// output
// 3 1 2 5 4
// 3 1 4 2 5
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;


int N, M, V;
vector<int> G[1001];
bool visit[1001];

void input() {
	
	cin >> N >> M >> V;
	for (int i = 0; i < M; i++) {
		int a, b;
		cin >> a >> b;
		G[a].push_back(b);
		G[b].push_back(a);
	}
}

void G_sort() {

	for (int i = 0; i < N; i++) {
		sort(G[i].begin(), G[i].end());
	}
}

void dfs(int num) {
	visit[num] = true;
	cout << num << ' ';
	
	for (int i = 0; i < G[num].size(); i++) {
		int next = G[num][i];
		if (!visit[next])
			dfs(next);
	}
}

int main() {

	input();
	G_sort();
	dfs(V);

	return 0;
}
