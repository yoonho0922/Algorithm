#include <iostream>
#include <queue>
using namespace std;
int main(){
	queue<int> q;
	q.push(1);
	q.push(2);
	q.push(3);
	q.push(4);
	
	q.pop();
	q.pop();
	
	//front
	cout<<"front element: "<<q.front()<<'\n';
	//back
	cout<<"back element: "<<q.back()<<'\n';
	//size
	cout<<"queue size: "<<q.size()<<'\n';
	
	return 0;
}
