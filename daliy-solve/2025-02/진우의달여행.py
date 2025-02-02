# https://www.acmicpc.net/problem/17484

MAX = 999

N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]

dp = [[[MAX] * 3 for _ in range(M + 2)] for _ in range(N)]
for i in range(1, M + 1):
    for j in range(3):
        dp[0][i][j] = G[0][i - 1]

for i in range(1, N):
    for j in range(1, M + 1):
        # 좌
        dp[i][j][0] = G[i][j-1] + min(dp[i-1][j+1][1], dp[i-1][j+1][2])
        # 중
        dp[i][j][1] = G[i][j-1] + min(dp[i-1][j][0], dp[i-1][j][2])
        # 우
        dp[i][j][2] = G[i][j-1] + min(dp[i-1][j-1][0], dp[i-1][j-1][1])

answer = MAX
for i in range(1, M + 1):
    answer = min(answer, min(dp[N-1][i]))
print(answer)
