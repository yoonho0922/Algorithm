# https://www.acmicpc.net/problem/13699

N = int(input())

dp = [0] * (N+1)
dp[0] = 1

for i in range(1, N+1):
    for j in range(i):
        dp[i] += dp[j] * dp[i-1-j]

print(dp[N])