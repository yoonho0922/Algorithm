# https://www.acmicpc.net/problem/16395

N, K = map(int, input().split())

d = [[1] * i for i in range(1, N+1)]

for i in range(1, N):
    for j in range(1, i):
        d[i][j] = d[i-1][j-1] + d[i-1][j]

print(d[N-1][K-1])