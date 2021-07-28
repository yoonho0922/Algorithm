import heapq
import sys
readline = sys.stdin.readline
INF=99999999

def dijkstra(s, e):
    q = []
    dist = [INF]*(N+1)

    dist[s] = 0
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

    return dist[E]


N = int(readline())
M = int(readline())
G = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, cost = map(int, readline().split())
    G[s].append((e, cost))
S, E = map(int, readline().split())

print(dijkstra(S, E))