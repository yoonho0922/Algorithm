# https://www.acmicpc.net/problem/5972

import heapq
INF = 1e9

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, weight = map(int, input().split())
    G[a].append([b, weight])
    G[b].append([a, weight])

dists = [INF] * (N+1)
dists[1] = 0
q = [[0, 1]]

while q:
    cur_dist, cur_node = heapq.heappop(q)
    for next_node, next_weight in G[cur_node]:
        if cur_dist + next_weight < dists[next_node]:
            dists[next_node] = cur_dist + next_weight
            heapq.heappush(q, [dists[next_node], next_node])

print(dists[N])
