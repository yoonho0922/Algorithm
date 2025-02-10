# https://www.acmicpc.net/problem/1312

A, B, N = map(int, input().split())

print(((A * pow(10, N) ) // B)%10)