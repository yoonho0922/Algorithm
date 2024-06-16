# https://www.acmicpc.net/problem/1509

INF = 1e9

S = input()
N = len(S)

# 팰린드롬 P 구하기
P = [[False] * (N) for _ in range(N)]

for gap in range(0, N):
    for l in range(N):
        if not(l + gap < N):
            break

        if gap == 0:
            P[l][l] = True
        elif gap == 1:
            if S[l] == S[l + 1]:
                P[l][l + 1] = True
        else:
            if S[l] == S[l + gap] and P[l+1][l + gap -1]:
                P[l][l + gap] = True

# 최소 분할 구하기
dp = [1e9] * N
dp[0] =1

for end in range(1, N):
    for start in range(end + 1):
        if P[start][end]:
            if start == 0:
                dp[end] = 1
            else:
                dp[end] = min(dp[end], dp[start-1] + 1)
print(dp[N-1])