# https://www.acmicpc.net/problem/2740

N, M = map(int, input().split())
G1 = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
G2 = [list(map(int, input().split())) for _ in range(M)]

G3 = [[] for _ in range(N)]

for i in range(N):
    for j in range(K):
        x = 0
        for k in range(M):

            x += G1[i][k] * G2[k][j]
        G3[i].append(x)

for row in G3:
    print(*row)