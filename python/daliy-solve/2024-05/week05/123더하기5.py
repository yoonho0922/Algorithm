# https://www.acmicpc.net/problem/15990

MAX_VALUE  = 100_000
DIVISION = 1_000_000_009

dp = [[] for _ in range(MAX_VALUE+1)]
dp[1]= [0,1,0,0]
dp[2] = [0,0,1,0]
dp[3] = [0,1,1,1]

for i in range(4, MAX_VALUE+1):
    add_1 = (dp[i-1][2] + dp[i-1][3])%DIVISION
    add_2 = (dp[i-2][1] + dp[i-2][3])%DIVISION
    add_3 = (dp[i-3][1] + dp[i-3][2])%DIVISION

    dp[i] = [0, add_1, add_2, add_3]

T = int(input())
for _ in range(T):
    x = int(input())
    print(sum(dp[x])%DIVISION)
