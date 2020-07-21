#include <iostream>
#include <string>
#include <stack>
#include <iterator>
#include <vector>
#include <map>
using namespace std;

int main()
{
   vector<int> v(5, 0); // size, value로 초기화
   v.push_back(1); // 벡터의 뒤에 원소 삽입
   v.push_back(1);
   v.push_back(1);
   v.pop_back(); // 맨 끝에 있는 원소 삭제
   v.insert(v.begin() + 3, 23);
   v.erase(v.begin() + 3);
   cout << v.size(); // 벡터의 크기
   vector<int> ::iterator iter; // 컨테이너 타입 :: iterator q변수 선언

   for (int i = 0; i < v.size(); i++)
   {
      cout << v[i] << " "; // 벡터는 배열의 특성을 가지고 있어서 index로 값에 접근이 가능하다
   }

   for (iter = v.begin(); iter != v.end(); iter++)
   {
      cout << *iter << " ";
   }
   map<int, int> m;
   m.insert({1, 1});

   m[1] = 6;
   m.insert({ 1, 2});
   map<int, int> ::iterator iter2;
   //cout << iter2->first;
   /*for (int i = 0; i < m.size(); i++)
   {
      cout << m[i];
   }*/  // Error 발생

   for (iter2 = m.begin(); iter2 != m.end(); iter2++)
   {
      cout << iter2->first << " " << iter2->second; // vector를 제외한 나머지 컨테이너에서 탐색을 하려면 무조건 iterator를 사용해야한다.
   }
   
   string s = ""; // string은 기본적으로 vector와 비슷
   s += "string";
   s.push_back('s');

   s.pop_back();
   cout << " : " << "\n";
   cout << s.find("str");
   string s2 = s.substr(0, 3); // s의 0번째부터 2번째까지 값을 s2로 저장
   string s3 = s.substr(s.find("strin"));

   /* vector와 마찬가지로 iterator로 접근도 가능 */
   // string :: iterator iter3 = s.begin()
   for (auto iter3 = s.begin(); iter3 != s.end(); iter3++)
   {
      cout << *iter3;
   }

   stack<int> st; // 디폴트로 deque로 구현이 된다. 순차 컨테이너만 가능.
   st.push(1);
   return 0;
}
