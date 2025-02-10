# https://www.acmicpc.net/problem/11660

import sys
readline = sys.stdin.readline


def get_sum(graph, x1, y1, x2, y2):
    result = 0
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            result += graph[i-1][j-1]
    return result


def get_dp(graph, size):
    dp = [[0]*(size+1) for _ in range(size+1)]

    for i in range(1, size+1):
        for j in range(1, size+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + graph[i-1][j-1]

    return dp


def get_partial_sum(dp, x1, y1, x2, y2):
    return dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]


N, M = map(int, readline().split())

G = []

for _ in range(N+1):
    row = list(map(int, readline().split()))
    G.append(row)

dp = get_dp(graph=G, size=N)

for _ in range(M):
    x1, y1, x2, y2 = map(int, readline().split())

    print(get_partial_sum(dp=dp, x1=x1, y1=y1, x2=x2, y2=y2))