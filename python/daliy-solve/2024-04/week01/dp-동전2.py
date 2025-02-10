# https://www.acmicpc.net/problem/2294

INF = 1e9

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
dp = [-1] * (K+1)

for i in range(1, K+1):
    min_value = INF

    for c in coins:
        if not (0<= i-c < K+1):
            continue

        if c == i:
            min_value = 1
            break
        if dp[i-c] != -1:
            min_value = min(min_value, 1 + dp[i-c])

    if min_value != INF:
        dp[i] = min_value

print(dp[K])