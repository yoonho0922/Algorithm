# https://www.acmicpc.net/problem/1446

INF = 1e9

N, D = map(int, input().split())
G = [[0, 0, 0]]
for _ in range(N):
    s, e, cost = map(int, input().split())
    if e <= D:
        G.append([s, e, cost])
G.append([D, D, 0])

G.sort(key=lambda x: [x[1], x[0]])

d = [INF] * (len(G))
d[0] = 0

for i in range(1, len(G)):
    for j in range(i):
        if G[j][1] <= G[i][0]:
            normal = d[j] + (G[i][1] - G[j][1])
            shortcut = d[j] + (G[i][0] - G[j][1]) + G[i][2]
            d[i] = min(d[i], normal, shortcut)

print(d[-1])