#include<iostream>
#include<vector>
using namespace std;

int main(){
	int N, M, x, sum, res = 0;
	int d = 0;
	vector<int> v;
	cin>>N>>M;
	
	for(int i=0; i<N; i++){
		cin>>x;
		v.push_back(x);
	}
	
	for(int i=0; i<N-2; i++){	// 5,6,7
		for(int j=i+1; j<N-1; j++){	// 6,7,8 
			for(int k=j+1; k<N; k++){ // 7,8,9
				sum = v[i]+v[j]+v[k];
				if(sum>res && sum<=M)
					res = sum;
			}
		}
	}
	
	cout<<res;
	
	return 0;	
}
