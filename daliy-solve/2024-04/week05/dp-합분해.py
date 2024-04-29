# https://www.acmicpc.net/problem/2225

N, K = map(int, input().split())

d = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, K+1):
    d[1][i] = i
for i in range(1, N+1):
    d[i][1] = 1

for i in range(2, N+1):
    for j in range(2, K+1):
        d[i][j] = (d[i-1][j] + d[i][j-1]) % 1000000000

print(d[N][K])