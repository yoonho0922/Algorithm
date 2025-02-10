# https://www.acmicpc.net/problem/9095

import sys
readline = sys.stdin.readline

T = int(input())
N = 10
dp = [0] * (N+1)
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, N+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(T):
    x = int(readline())
    print(dp[x])