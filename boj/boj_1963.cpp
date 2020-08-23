#include<iostream>
#include<string>
#include<cstring>
#include<queue>
using namespace std;

bool prime[10000];
int T, dist[10000];
string start_num, end_num;

void eratos() {
	for (int i = 0; i < 10000; i++)
		prime[i] = true;

	for (int i = 2; i < 10000; i++) {
		if (prime[i] == false) continue;

		for (int j = i + i; j < 10000; j += i)
			prime[j] = false;
	}
}

void bfs(string start_num) {
	queue<string> q;
	memset(dist, -1, sizeof(dist));

	q.push(start_num);
	dist[stoi(start_num)] = 0;

	while (!q.empty()) {
		string curr_num = q.front();
		q.pop();
		for (int i = 0; i < 4; i++) {
			string next_num = curr_num;
			for (int j = 0; j < 10; j++) {
				next_num[i] = j + '0';
				int tmp = stoi(next_num);

				if (tmp < 1000 || tmp>9999) continue; // 범위 넘는 경우 제외

				if (dist[tmp] == -1 && prime[tmp]) { // 소수이고 방문 안한 경우
					dist[stoi(next_num)] = dist[stoi(curr_num)] + 1;
					q.push(next_num);
				}

				if (next_num == end_num && prime[tmp]) {	// 도달한 경우
					cout << dist[stoi(next_num)]<<'\n';
					return;
				}
			}
		}
	}
	cout << "Impossible";
	return;
}

int main() {
	eratos();
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> start_num >> end_num;
		bfs(start_num);
	}

	return 0; 
}
