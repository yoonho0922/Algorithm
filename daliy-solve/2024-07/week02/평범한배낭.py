# https://www.acmicpc.net/problem/12865

N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (K+1) for _ in range(N+1)]
# dp[i]: i 번째 아이템 까지 썼을 때 허용 가능 무게 별 가치

for i in range(1, N+1):
    weight, valuable = items[i-1]
    # j: 허용 가능한 무게
    for j in range(1, K+1):
        if j-weight >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - weight] + valuable)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])
