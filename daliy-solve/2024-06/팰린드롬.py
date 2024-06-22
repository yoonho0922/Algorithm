# https://www.acmicpc.net/problem/10942

import sys
readline = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))
M = int(input())

P = [[False] * N for _ in range(N)]

for gap in range(N):
    for start in range(N - gap):
        end = start + gap

        if gap == 0:
            P[start][end]  = True
        elif gap == 1:
            if S[start] == S[end]:
                P[start][end] = True
        else:
            if S[start] == S[end] and P[start+1][end-1]:
                P[start][end] = True


for _ in range(M):
    s, e = map(int, readline().split())
    if P[s-1][e-1]:
        print(1)
    else:
        print(0)