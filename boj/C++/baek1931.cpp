// 1. fin 순으로 정렬해서 회의를 선택하는게 핵심
// 2. fin이 같고 start가 이전 회의의 fin 이상이면 카운트
//    이때, 해당 조건을 만족하면 조건을 만족하는 회의가 몇개가 있든
//	  하나만 카운트하고 넘기면 됨 (단, 3번은 예외 - 이 문제의 핵심)
// 3. start와 fin이 같은 회의를 카운트 해야하는 것을 고려
// 4. O(n log n)알고리즘, 그리디 알고리즘 (N^2은 시간 초과)

#include<iostream>
#include<utility>
#include<algorithm>
using namespace std;

pair <int, int> p[100001];
int N, now, total = 0;

bool cmp_fin(pair<int, int> a, pair<int, int> b) { return a.second < b.second; }
bool cmp_start(pair<int, int> a, pair<int, int> b) { return a.first < b.first; }

int main() {
	
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> p[i].first >> p[i].second;
	}

	// 끝나는 시간 순으로 정렬
	sort(p, p + N, cmp_fin);

	for (int i = 0; i < N; i++) {
		if (now <= p[i].first) {
			int select = i, j = i+1;

			// 끝나는 시간이 같을 때, 시작 시간 순으로 정렬
			while ( p[i].second == p[j].second && j < N) {
				j++;
			}
			sort(p + i, p + j, cmp_start);
			
			now = p[i].second;
			total++;
		}
	}

	cout << total;

	return 0;
}