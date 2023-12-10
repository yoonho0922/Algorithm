#include<iostream>
#include<algorithm>
using namespace std;

int N;
pair<int, int> p[100001];

void input() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		int x, y;
		cin >> x >> y;
		p[i] = make_pair(x, y);
	}
}

int main() {
	input();
	sort(p, p + N);
	for (int i = 0; i < N; i++) {
		cout << p[i].first << ' ' << p[i].second;
		cout << '\n';
	}
	return 0;
}