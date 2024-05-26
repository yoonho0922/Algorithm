# https://www.acmicpc.net/problem/11404

INF = 1e9

N = int(input())
M = int(input())
G = [[INF]*(N+1) for _ in range(N+1)]

for _ in range(M):
    u, v, cost = map(int, input().split())
    G[u][v] = min(G[u][v], cost)

for i in range(1, N+1):
    for j in range(1, N+1):
        if i==j:
            G[i][j]  = 0

for i in range(1, N+1):
    for s in range(1, N+1):
        for e in range(1, N+1):
            G[s][e] = min(G[s][e], G[s][i] + G[i][e])

for i in range(1,N+1):
    for j in range(1, N+1):
        if G[i][j] >= INF:
            print(0, end = ' ')
        else:
            print(G[i][j],end=' ')
    print()