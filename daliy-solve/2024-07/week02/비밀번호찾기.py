# https://www.acmicpc.net/problem/17219

N, M = map(int, input().split())
pws = {}

for _ in range(N):
    site, pw = input().split()
    pws[site] = pw

for _ in range(M):
    site = input()
    print(pws[site])