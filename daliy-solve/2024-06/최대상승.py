# https://www.acmicpc.net/problem/25644

N = int(input())
S = list(map(int,input().split()))

dp=[0]*N
now_min = S[0]

for i in range(1, N):
    now_min = min(now_min, S[i])
    dp[i] = max(dp[i-1], S[i]-now_min)

print(dp[N-1])