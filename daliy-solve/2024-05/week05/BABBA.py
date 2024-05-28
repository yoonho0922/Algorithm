# https://www.acmicpc.net/problem/9625

N = int(input())
dp = [[1,0], [0, 1]]

for i in range(2, N+1):
    dp.append([sum(x) for x in zip(dp[i-1], dp[i-2])])

print(' '.join(map(str,dp[N])))