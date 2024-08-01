# https://www.acmicpc.net/problem/9507

MAX = 67

def koong(n):
    if dp[n] != -1:
        return dp[n]
    else:
        dp[n] = koong(n-1) + koong(n-2) + koong(n-3) + koong(n-4)
        return dp[n]


dp = [1, 1, 2, 4] + [-1] * (MAX - 3)

T = int(input())
for _ in range(T):
    N = int(input())
    print(koong(N))