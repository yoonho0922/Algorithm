# 이코테 p.223

N = int(input())

dp = [0] * (N+1)
dp[1] = 1
dp[2] = 3

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]*2

print(dp[N]%796796)