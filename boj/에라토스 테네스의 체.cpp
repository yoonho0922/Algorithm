#include<iostream>
using namespace std;

bool arr[10001];

void eratos()
{
    for (int i = 1; i < 10000; i++)
    {
        arr[i] = true;
    }

    for (int i = 2; i < 10000; i++)
    {
        if (arr[i] == false) continue;

        for (int j = i + i; j < 10000; j += i)
            if (arr[j] == true) arr[j] = false;
    }
}

int main()
{
    eratos();

    for (int i = 2; i < 10000; i++) {
        if (arr[i])
            cout << i << ' ';
    }

    return 0;
}