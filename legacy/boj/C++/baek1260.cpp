#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
#include<cstring>
using namespace std;

vector<int> graph[1001];
bool visit[1001];
int dist[1001];

int N, M, V;


void input() {
	cin >> N >> M >> V;
	for (int i = 0; i < M; i++) {
		int a, b;
		cin >> a >> b;
		graph[a].push_back(b);
		graph[b].push_back(a);
		}
	for (int i = 1; i <= N; i++) 
		sort(graph[i].begin(), graph[i].end());
}

void dfs(int num) {
	visit[num] = true;
	cout << num << " ";
	for (int i = 0; i < graph[num].size(); i++) {
		
		int next = graph[num][i];

		if (!visit[next])
			dfs(next);
	}
}

void bfs(int num) {
	queue<int> q;
	dist[num] = 0;
	q.push(num);

	while (!q.empty()) {

		int curr = q.front();
		cout << curr << " ";
		q.pop();

		for (int i = 0; i < graph[curr].size(); i++) {
			
			int next = graph[curr][i];
			if (dist[next] == -1) {
				dist[next] = dist[curr] + 1;
				q.push(next);
			}
		}
	}
}

int main() {

	input();
	dfs(V);
	cout << '\n';
	memset(dist, -1, sizeof(dist));
	bfs(V);

	return 0;
}