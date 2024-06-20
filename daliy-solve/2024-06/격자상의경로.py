# https://www.acmicpc.net/problem/10164

N, M, K = map(int,input().split())
cy, cx = [(K-1)//M, (K-1)%M] if K != 0 else [N-1 , M-1]

dp = [[0]*M for _ in range(N)]
dp[0][0] = 1

for i in range(cy+1):
    for j in range(cx+1):
        if i > 0:
            dp[i][j] += dp[i-1][j]
        if j > 0:
            dp[i][j] += dp[i][j-1]


for i in range(cy, N):
    for j in range(cx, M):
        if i > cy:
            dp[i][j] += dp[i-1][j]
        if j > cx:
            dp[i][j] += dp[i][j-1]

print(dp[N-1][M-1])