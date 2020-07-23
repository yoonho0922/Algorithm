#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool compare(int a, int b){
	if(a>b)
		return true;
	else
		return false;
}

int main(){
	vector<int> v;
	v.push_back(1);
	v.push_back(5);	
	v.push_back(3);
	v.push_back(2);
	v.push_back(7);
	
	//algorithm - sort
	sort(v.begin(), v.end()); // unstable sort, sort(v.begin(), v.end(), compare) : 내림차순  
	
	for(int i = 0; i<v.size(); i++){
		cout<<v[i]<<' ';
	}
	
	//algorithm - max_element
	int max = *max_element(v.begin(), v.end());
	cout<<'\n'<<max<<'\n'; 
	
	//container - pair
	pair<int,int> p; // first, second
	p.first = 2;
	p.second = 0;
	
	cout<<p.first<<','<<p.second;
	
	return 0;
}
