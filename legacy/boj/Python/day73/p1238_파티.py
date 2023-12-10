import heapq
import sys
readline = sys.stdin.readline

INF = 99999999

def dijkstra(s, e):
    q = []
    dist = [INF]*(N+1)

    dist[s]=0
    heapq.heappush(q, (dist[s], s))

    while q:
        cur_dist, cur_v = heapq.heappop(q)
        if dist[cur_v] < cur_dist:
            continue

        for next_v, next_cost in G[cur_v]:
            cost = cur_dist + next_cost
            if cost < dist[next_v]:
                dist[next_v] = cost
                heapq.heappush(q, (dist[next_v], next_v))

    if e==-1:
        return dist
    else:
        return dist[e]


N, M, X = map(int, readline().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, cost = map(int, readline().split())
    G[a].append((b, cost))

back = dijkstra(X, -1)

for i in range(1, N+1):
    back[i] += dijkstra(i, X)

print(max(back[1:]))