# https://www.acmicpc.net/problem/16194

N = int(input())
P = list(map(int, input().split()))

dp = [0] * (N+1)

for i in range(1, N+1):
    dp[i] = P[i-1]

    for j in range(1, i):
        dp[i] = min(dp[i], dp[j] + dp[i-j])

print(dp[N])