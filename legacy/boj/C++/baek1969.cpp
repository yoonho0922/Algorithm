#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

char a[1000][50], s[50];
int hd_total, N, M;

void select_base(vector<int> base, int i) {
	char acgt[4] = { 'A', 'C', 'G', 'T' };
	int sub = base[0];
	s[i] = acgt[0];

	for (int k = 0; k < 3; k++) {

		if (sub < base[k + 1]) {
			s[i] = acgt[k + 1];
			sub = base[k + 1];	// i번째 열에 같은 염기의 갯수
		}
	}
	hd_total = hd_total - sub;
}

int main() {
	cin >> N >> M;
	hd_total = N * M;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> a[i][j];
		}
	}

	for (int i = 0; i < M; i++) {
		vector<int> base(4,0);
		for (int j = 0; j < N; j++) {	// i 번째 염기 개수 체크
			if (a[j][i] == 'A') {
				base[0]++;
			}
			else if (a[j][i] == 'C') {
				base[1]++;
			}
			else if (a[j][i] == 'G') {
				base[2]++;
			}
			else if (a[j][i] == 'T') {
				base[3]++;
			}
		}
		select_base(base, i);	// s의 i번째 염기 결정
	}


	for (int i = 0; i < M; i++) {
		cout << s[i];
	}
	cout << '\n' << hd_total;
	
	return 0;
}