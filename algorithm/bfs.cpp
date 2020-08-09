// BFS
// input
// 5 5 3
// 5 4
// 5 2
// 1 2
// 3 4
// 3 1
// output
// 3 1 4 2 5
#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>
#include<queue>
using namespace std;

int N, M, V;
vector<int> G[1001];
int dist[1001];
queue<int> q;



void input() {
	cin >> N >> M >> V;
	for (int i = 0; i < M; i++) {
		int a, b;
		cin >> a >> b;
		G[a].push_back(b);
		G[b].push_back(a);
	}
	for (int i = 1; i <= N; i++)
		sort(G[i].begin(), G[i].end());
}

void bfs(int num) {
	dist[num] = 0;
	q.push(num);

	while (!q.empty()) {
		int curr = q.front(); q.pop();
		cout << curr << " ";
		for (int i = 0; i < G[curr].size(); i++) {
			int next = G[curr][i];
			if (dist[next] == -1) {
				q.push(next);
				dist[next] = dist[curr] + 1;
			}	
		}
	}
}

int main() {

	input();
	cout << '\n';
	memset(dist, -1, sizeof(dist));
	bfs(V);

	return 0;
}