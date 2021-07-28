import heapq
import sys
readline=sys.stdin.readline
INF = 999999999

def bfs(start):
    q=[]
    dist[start] = 0
    heapq.heappush(q, (dist[start], start))

    while q:
        cur_dist, cur_node = heapq.heappop(q)

        if dist[cur_node] < cur_dist:
            continue
        for v, w in G[cur_node]:
            cost = cur_dist + w
            if cost < dist[v]:
                dist[v]=cost
                heapq.heappush(q, (dist[v], v))


V, E = map(int, readline().split())
K = int(readline())
G = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, readline().split())
    G[a].append((b,c))

dist = [INF]*(V+1)

bfs(K)
for i in dist[1:]:
    print(i if i != INF else 'INF')