import heapq
import sys
readline = sys.stdin.readline
INF = 100000000

N = int(readline())
M = int(readline())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
for _ in range(M):
    a, b, c = map(int, readline().split())
    graph[a].append((b, c))
start, end = map(int, readline().split())

def dijkstra(start):
    q = []

    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        cur_dist, cur_v = heapq.heappop(q)

        for v, w in graph[cur_v]:
            cost = cur_dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))

dijkstra(start)
print(distance[end])

