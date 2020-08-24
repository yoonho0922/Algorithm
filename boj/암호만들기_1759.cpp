#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int L, C;
char letter[16];
bool visit[16];
vector<char> v;

void input() {
	cin >> L >> C;
	for (int i = 0; i < C; i++)
		cin >> letter[i];
	sort(letter, letter + C);
}

bool promising(int cnt) {
	int co = 0, vo = 0; // 자음, 모음

	for (int j = 0; j < C; j++) {
		if (visit[j]) {
			if (letter[j]== 'a' || letter[j] == 'e' || letter[j] == 'i'
				|| letter[j] == 'o' || letter[j] == 'u')
				vo++;
			else
				co++;
		}
	}

	if (co >= L || vo >= L - 1) //조건을 만족 못하는 경우
		return false;
	else
		return true;
}

void go(int idx, int cnt) {
	if (!promising(cnt)) return;

	if (cnt == L) {
		for(int j = 0; j<C; j++)
			if (visit[j])
				cout << letter[j];
		cout << '\n';
		return ;
	}
	for (int i = idx; i < C; i++) {
		if (visit[i]) continue;

		visit[i] = true;
		go(i, cnt + 1);
		visit[i] = false;
	}
}

int main() {
	input();
	go(0, 0);

	return 0;
}