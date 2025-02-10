# https://www.acmicpc.net/problem/9252


def trace(cy, cx):
    if dp[cy][cx] == 0:
        return

    if dp[cy][cx] == dp[cy-1][cx]:
        trace(cy-1, cx)
    elif dp[cy][cx] == dp[cy][cx-1]:
        trace(cy, cx-1)
    else:
        ans.append(B[cx-1])
        trace(cy-1, cx-1)

A = input()
B = input()

N = len(A)
M = len(B)
dp = [[0] * (M + 1) for i in range(N + 1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

ans = []
trace(N, M)

print(dp[N][M])
print(''.join(reversed(ans)))