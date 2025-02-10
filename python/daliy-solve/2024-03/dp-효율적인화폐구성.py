# 이코테 p.226

import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
coins = []
for _ in range(N):
    coins.append(int(readline()))

dp = [-1] * 10001

for coin in coins:
    dp[coin] = 1

for i in range(min(coins)+1, M+1):
    # 분할 정복할 수 있는 코인
    subtractable_coins = [coin for coin in coins if i - coin >= 0 and dp[i-coin] != -1]

    if subtractable_coins:
        dp[i] = min(list(dp[i-coin] for coin in subtractable_coins)) + 1

print(dp[M])