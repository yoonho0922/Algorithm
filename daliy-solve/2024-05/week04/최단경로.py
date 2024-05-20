# https://www.acmicpc.net/problem/1753

import heapq
import sys
readline = sys.stdin.readline

INF = 1e9

def get_shortest(V, S, G):
    dists = [INF] * (V+1)
    q = []

    dists[S] = 0
    heapq.heappush(q, [0,S])

    while q:
        cost, now = heapq.heappop(q)

        for next, next_cost in G[now]:
            new_cost = cost + next_cost

            if new_cost < dists[next]:
                dists[next] = new_cost
                q.append([new_cost, next])

    return dists

V, E = map(int, input().split())
S = int(input())
G = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, readline().split())
    G[u].append([v,w])

dists = get_shortest(V, S, G)

for i in range(1, V+1):
    print(dists[i] if dists[i] < INF else 'INF')