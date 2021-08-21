import sys
readline = sys.stdin.readline
INF = 99999999

N, M = map(int, readline().split())
G = []
for _ in range(M):
    a, b, c = map(int, readline().split())
    G.append([a, b, c])

dist = [INF] * (N+1)
dist[1] = 0

for i in range(N):
    for j in range(M):
        cur, next, cost = G[j]

        if dist[cur] != INF and dist[cur] + cost < dist[next]:
            dist[next] = dist[cur] + cost

            if i == N - 1:
                print(-1)
                exit()

for i in range(2, N+1):
    print(dist[i] if dist[i] != INF else -1)
