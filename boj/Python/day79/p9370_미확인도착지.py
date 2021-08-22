import heapq
import sys
readline = sys.stdin.readline
INF = 999999999


def dijkstra(s, e):
    dist = [INF] * (n + 1)
    q = []

    dist[s] = 0
    heapq.heappush(q, (dist[s], s))

    while q:
        cur_dist, cur_node = heapq.heappop(q)

        for next_node, cost in G[cur_node]:
            if cur_dist + cost < dist[next_node]:
                dist[next_node] = cur_dist + cost
                heapq.heappush(q, (dist[next_node], next_node))

    return dist[e]


T = int(readline())
for _ in range(T):
    n, m, t = map(int, readline().split())
    s, g, h = map(int, readline().split())

    G = [[] for _ in range(n+1)]
    gh_cost = 0

    for _ in range(m):
        a, b, c = map(int, readline().split())
        if [a,b]==[g,h] or [a,b]==[h,g]:
            gh_cost = c
        G[a].append((b, c))
        G[b].append((a, c))

    ans = []

    for _ in range(t):
        candi = int(readline())

        min_dist = dijkstra(s, candi)
        gh_dist = dijkstra(s, g) + gh_cost + dijkstra(h, candi)
        hg_dist = dijkstra(s, h) + gh_cost + dijkstra(g, candi)

        if min_dist in [gh_dist, hg_dist]:
            ans.append(candi)

    ans.sort()
    print(*ans)




