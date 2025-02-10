# https://www.acmicpc.net/problem/1753
# 최단경로

import heapq
import sys

readline = sys.stdin.readline
INF = 1e9


def get_dists():
    dists = [INF] * (V + 1)
    q = []

    # 시작점의 거리는 0으로 초기화하고 q에 삽입
    dists[S] = 0
    heapq.heappush(q, (dists[S], S))

    # q가 비워질 때 까지 초기화 반복
    while q:
        now_dist, now = heapq.heappop(q)

        # 최단 거리가 이미 결정됐다면 무시
        if dists[now] < now_dist:
            continue

        # 현재 노드에서 갈 수 있는 노드 검사
        for next, next_weight in graph[now]:
            # 현재 경로가 최단 거리라면 최단거리를 갱신하고 q에 삽입
            if now_dist + next_weight < dists[next]:
                dists[next] = now_dist + next_weight
                heapq.heappush(q, (now_dist + next_weight, next))

    # 거리 반환
    return dists


V, E = map(int, readline().split())
S = int(readline())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    start, end, weight = map(int, readline().split())
    graph[start].append([end, weight])

dists = get_dists()

for dist in dists[1:]:
    if dist == INF:
        print('INF')
    else:
        print(dist)
