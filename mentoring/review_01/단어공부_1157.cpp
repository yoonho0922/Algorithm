#include<iostream>
using namespace std;

string s;
int m, check[100];
char res;

int main() {

	cin >> s;
	for (int i = 0; i < s.size(); i++) {
		s[i] = toupper(s[i]);
		check[(int)s[i]]++;
	}

	for (int i = 'A'; i <= 'Z'; i++) {
		if (m < check[i]) {
			m = check[i];
			res = i;
		}
		else if (check[i] == m)
			res = '?';
	}

	cout << res;

	return 0;
}