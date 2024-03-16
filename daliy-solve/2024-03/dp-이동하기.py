# https://www.acmicpc.net/problem/11048

import sys

readline = sys.stdin.readline


N, M = map(int, readline().split())
G = [list(map(int,readline().split())) for _ in range(N)]

dp = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + G[i-1][j-1]

print(dp[N][M])