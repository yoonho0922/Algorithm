#include<iostream>
using namespace std;

string day[7] = { "SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT" };
int x, y, day_total;
int month[13] = { 0,31,28,31,30,31,30,31,31,30,31,30,31 };

int main() {
	cin >> x >> y;
	for (int i = 1; i < x; i++) 
		day_total += month[i];
	day_total += y;

	cout << day[day_total % 7];

	return 0;
}