# https://www.acmicpc.net/problem/1509

INF = 1e9


S = input()
N = len(S)

P = [[False] * N for _ in range(N)]

# row: start, column: end
for gap in range(N):
    for start in range(N-gap):
        if gap == 0:
            P[start][start] = True
        elif gap == 1:
            if S[start] == S[start+gap]:
                P[start][start+gap] = True
        else:
            if S[start] == S[start+gap] and P[start+1][start+gap-1]:
                P[start][start+gap] = True

dp = [INF] * N
dp[0] = 1

for i in range(1, N):
    for start in range(i+1):
        if P[start][i]:
            if start == 0:
                dp[i] = 1
                break
            else:
                dp[i] = min(dp[i], dp[start-1] + 1)

print(dp[N-1])