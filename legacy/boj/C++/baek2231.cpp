#include<iostream>
using namespace std;

int main() {
	int N, dec, con = 0;
	cin >> N;

	for (int i = 1; i < 1000000; i++) {
		dec = i + i / 100000 % 10 + i / 10000 % 10 + i / 1000 % 10 + i / 100 % 10 + i / 10 % 10 + i % 10;
		if (N == dec) {
			con = i;
			break;
		}
	}
	cout << con;
	return 0;
}