# https://www.acmicpc.net/problem/11722

N = int(input())

dp = [0] * 1001
dp[1], dp[2] = 1, 2

for i in range(3, N+1):
    dp[i] = min(dp[i-1] + 1, dp[i-3] + 1)

if dp[N] % 2 == 1:
    print('SK')
else:
    print('CY')