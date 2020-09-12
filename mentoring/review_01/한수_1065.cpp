#include<iostream>
using namespace std;

int N, res;

int main() {
	cin >> N;

	for (int i = 1; i <= N; i++) {
		if (i < 100) {
			res++;
			continue;
		}
		int a = i / 100;
		int b = i % 100 / 10;
		int c = i % 10;
		if (b*2 == (a + c)) 
			res++;
	}

	cout << res;

	return 0;
}