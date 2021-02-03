import sys
readline = sys.stdin.readline

T = int(readline())
dp = [0, 1, 2, 4]

for _ in range(T):
    N = int(readline())

    while len(dp) < N + 1:
        i = len(dp)
        dp.append(dp[i-3] + dp[i-2] + dp[i-1])

    print(dp[N])
