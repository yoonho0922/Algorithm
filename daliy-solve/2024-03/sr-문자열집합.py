# https://www.acmicpc.net/problem/14425

import sys
readline = sys.stdin.readline

N, M = map(int, input().split())
S = dict(readline() for _ in range(N))

count = 0

for _ in range(M):
    target = readline()
    if S[target]:
        count+=1
print(count)