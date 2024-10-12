# https://www.acmicpc.net/problem/24313

a1, a2 = map(int, input().split())
c = int(input())
n0 = int(input())

if a2 <= (c - a1) * n0:
    print(1)
else:
    print(0)