#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
	int x, sub, sum = 0, n1, n2;
	vector<int> v,r;
	
	for(int i=0; i<9; i++){
		cin>>x;
		v.push_back(x);
	}
	sort(v.begin(), v.end());
	
	for(int i=0; i<9; i++){
		sum += v[i];
	}
	for(int i=0; i<8; i++){ // index 0-7
		for(int j=i+1; j<9; j++){	// index 1-8
			sub = v[i] + v[j];
			if(sum-sub == 100){
				n1 = i;
				n2 = j;
			}
		}	
	}
	
	for(int i=0; i<9; i++){
		if(i != n1 && i != n2)
			cout<<v[i]<<'\n';
	}
	
	return 0;	
}
