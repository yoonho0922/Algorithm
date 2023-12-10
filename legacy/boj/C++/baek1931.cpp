// 1. fin ������ �����ؼ� ȸ�Ǹ� �����ϴ°� �ٽ�
// 2. fin�� ���� start�� ���� ȸ���� fin �̻��̸� ī��Ʈ
//    �̶�, �ش� ������ �����ϸ� ������ �����ϴ� ȸ�ǰ� ��� �ֵ�
//	  �ϳ��� ī��Ʈ�ϰ� �ѱ�� �� (��, 3���� ���� - �� ������ �ٽ�)
// 3. start�� fin�� ���� ȸ�Ǹ� ī��Ʈ �ؾ��ϴ� ���� ���
// 4. O(n log n)�˰���, �׸��� �˰��� (N^2�� �ð� �ʰ�)

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

	// ������ �ð� ������ ����
	sort(p, p + N, cmp_fin);

	for (int i = 0; i < N; i++) {
		if (now <= p[i].first) {
			int select = i, j = i+1;

			// ������ �ð��� ���� ��, ���� �ð� ������ ����
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