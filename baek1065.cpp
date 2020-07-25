#include<iostream>
#include<vector>
using namespace std;

int main() {
	int N, res = 0;
	cin >> N;	//N : 1~1000

	for (int i = 1; i < N + 1; i++) {
		if (i < 10) {
			res++;
		}
		else if (10 <= i && i < 100) {
			res++;
		}
		else if (100 <= i && i < 1000) {
			int a = i / 100, b = i / 10 % 10, c = i % 10;
			if (a-b == b-c)
				res++;
		}
	}
	cout << res;

	return 0;
}