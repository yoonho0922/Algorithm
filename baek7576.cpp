#include<iostream>
#include<queue>
using namespace std;

int M, N, G[1001][1001], res;
queue<pair<int,int>> q;
int dx[] = { 1,0,-1,0 }; // 오른쪽, 아래, 왼쪽, 위
int dy[] = { 0,1,0,-1 };

void input() {
	cin >> M >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> G[i][j];
			if (G[i][j] == 1)
				q.push(make_pair(i,j));
		}
	}
}

int main() {

	input();

	while (!q.empty()) {

		int ly = q.front().first, lx = q.front().second;
		q.pop();

		//printf("pop : %d, %d \n", ly, lx);

		for (int i = 0; i < 4; i++) {
			//cout << i<<' ';
			int cx = lx + dx[i];
			int cy = ly + dy[i];
			if (cx < 0 || cx >= M || cy < 0 || cy >= N) continue;
			
			if (G[cy][cx] == 0) {
				//printf("cy, cx : %d, %d \n", cy, cx);
				G[cy][cx] = G[ly][lx] + 1;
				//printf(" G : %d", G[cy][cx]);
				q.push(make_pair(cy, cx));
			}
		}
		//cout << '\n';
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			//cout << G[i][j] << ' ';

			if (G[i][j] == 0) {
				res = 0;
				goto EXIT;
			}
			else if (G[i][j] > res) {
				res = G[i][j];
			}
		}
		//cout << '\n';
	}
EXIT:
	cout << res-1;
	return 0;
}