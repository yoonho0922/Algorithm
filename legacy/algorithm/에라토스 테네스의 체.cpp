#include<iostream>
using namespace std;

bool prime[10000];

void eratos() {
	for (int i = 0; i < 10000; i++)
		prime[i] = true;

	for (int i = 2; i < 10000; i++) {
		if (prime[i] == false) continue;

		for (int j = i + i; j < 10000; j += i)
			prime[j] = false;
	}
}

int main() {
	eratos();

	for (int i = 2; i < 10000; i++) {
		if (prime[i]) {
			cout << i << ' ';
		}
	}

	return 0;
}
