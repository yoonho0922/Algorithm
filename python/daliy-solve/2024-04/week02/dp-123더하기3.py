# https://www.acmicpc.net/problem/15988

import sys
readline = sys.stdin.readline

MAX_NUM = 1000000

N = int(readline())
dp = [0]*(MAX_NUM+1)
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, MAX_NUM+1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])%1000000009

for _ in range(N):
    x = int(readline())
    print(dp[x])