# https://www.acmicpc.net/problem/18352
# 특정 거리의 도시 찾기

import heapq
import sys

readline = sys.stdin.readline
INF = 1e9


def get_shortest_dists():
    dists = [INF]*(N+1)
    q = []

    # 시작점 거리 초기화
    dists[X] = 0
    heapq.heappush(q, (0, X))

    while q:
        now_dist, now = heapq.heappop(q)

        # 이미 최단거리가 갱신됐다면 무시
        if dists[now] < now_dist:
            continue

        for next in graph[now]:
            next_dist = now_dist + 1

            # 현재 경로가 최단 경로라면 업데이트
            if next_dist < dists[next]:
                dists[next] = next_dist
                heapq.heappush(q, (next_dist, next))

    return dists


# 도시 수, 도로 수, 거리 정보, 시작점
N, M, K, X = map(int, readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, readline().split())
    graph[start].append(end)

# 각 도시의 최단거리를 구함
dists = get_shortest_dists()

# 거리가 K 도시를 오름차순으로 출력
results = [i for i in range(1, N+1) if dists[i] == K]
# results.sort()

if results:
    print("\n".join(map(str, results)))
else:
    print(-1)
