import heapq
import sys
readline = sys.stdin.readline

INF = 999999999

def dijkstra(s, e):
    q = []
    dist = [INF]*(N+1)

    dist[s] = 0
    heapq.heappush(q, (dist[s], s))

    while q:
        cur_cost, cur_v = heapq.heappop(q)

        if dist[cur_v] < cur_cost:
            continue

        for next_v, next_cost in G[cur_v]:
            cost = cur_cost + next_cost
            if cost < dist[next_v]:
                dist[next_v] = cost
                heapq.heappush(q, (dist[next_v], next_v))


    return dist[e] if dist[e] != INF else -1

N, M = map(int, readline().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, cost = map(int, readline().split())
    G[a].append((b, cost))
    G[b].append((a, cost))
V1, V2 = map(int, readline().split())

a, b, c = dijkstra(1, V1), dijkstra(V1, V2), dijkstra(V2, N)
e, f, g = dijkstra(1, V2), dijkstra(V2, V1), dijkstra(V1, N)

if -1 in [a, b, c]:
    print(-1)
else:
    print(min(a+b+c, e+f+g))