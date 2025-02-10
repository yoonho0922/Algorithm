# https://www.acmicpc.net/problem/2502


def get_ab(dp, D, K):
    for a in range(1, K//2+1):
        for b in range(a, K):
            if dp[D-3] * a + dp[D-2] * b == K:
                return a, b
            elif dp[D-3] * a + dp[D-2] * b > K:
                break
    return -1, -1

MAX_DAY = 30

D, K = map(int, input().split())


dp = [1, 1] + [0] * (MAX_DAY-2)

for i in range(2, MAX_DAY):
    dp[i] = dp[i-1] + dp[i-2]

a, b = get_ab(dp, D, K)
print(a)
print(b)