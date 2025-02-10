# 이코테 p.262
# 전보

import sys
import heapq
readline = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    dists = [INF] * (N+1)
    q = []

    # 시작점 초기화
    dists[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, cur = heapq.heappop(q)

        # 이미 방문한 노드면 무시 (꺼냈을 때 거리가 더 멀다면 이미 방문한 노드임)
        if dists[cur] < dist:
            continue

        # 인접한 노드 검사
        for next, cost in graph[cur]:
            next_dist = dists[cur] + cost

            if next_dist < dists[next]:
                dists[next] = next_dist
                heapq.heappush(q, (next_dist, next))

    return dists

N, M, C = map(int, readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, readline().split())
    graph[start].append([end, cost])


dists = dijkstra(C)

count = 0
max_time = 0

for dist in dists:
    # 시작노드를 제외하고 갈 수 있는 노드 검사
    if dist < INF and dist != 0:
        count += 1
        max_time = max(max_time, dist)

print(count, max_time)