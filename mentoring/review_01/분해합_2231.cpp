#include<iostream>
#include<string>
using namespace std;

int N;

int get_bunhae(int constructor) {
	int bunhae = constructor;
	string s = to_string(constructor);

	for (int i = 0; i < s.size(); i++)
		bunhae += s[i] - '0';
	return bunhae;
}

int brute() {
	for (int i = 1; i < N; i++) {
		if (get_bunhae(i) == N)
			return i;
	}
	return 0;
}

int main() {
	cin>>N;

	cout<<brute();

	return 0;
}