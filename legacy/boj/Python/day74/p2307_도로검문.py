import heapq
import sys
readline = sys.stdin.readline

INF = 99999999

def dijkstra(s, e, a, b):
    q = []
    dist = [INF]*(N+1)

    dist[s] = 0
    heapq.heappush(q, (dist[s], s))

    while q:
        cur_cost, cur_v = heapq.heappop(q)

        if dist[cur_v] < cur_cost:
            continue

        for next_v, next_cost in G[cur_v]:
            # 경찰이 막은 다리 라면
            if [cur_v, next_v] == [a, b] or [cur_v, next_v] == [b, a]:
                continue

            cost = cur_cost + next_cost
            if cost < dist[next_v]:
                dist[next_v] = cost
                heapq.heappush(q, (dist[next_v], next_v))

                E[next_v] = cur_v

    return dist[N]


N, M = map(int, readline().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, cost = map(int, readline().split())
    G[a].append((b, cost))
    G[b].append((a, cost))

E = [0]*(N+1) # 최단거리 경로
default_time = dijkstra(1, N, 0, 0)

ans, a = 0, N

while a !=0:
    b = E[a]
    police_time = dijkstra(1, N, a, b)

    if police_time == INF:
        ans = -1
        break

    ans = max(ans, police_time - default_time)
    a = b

print(ans)