
# 1. 가중치를 포함한 경로 저장
# 2. 노드 별 거리 테이블 0로 초기화
# 3. 시작점 거리=0, 시작점 큐에 넣음
# 4. 큐에서 꺼내 연결된 노드 확인, 거리 테이블 업데이트 및 연결된 노드 거리 낮은 순서로 넣기
# 5. 큐에서 꺼내기 반복

# 정점은 1부터

import heapq
import sys
readline = sys.stdin.readline

INF = 1e10


def get_shortest_dist(G, V, S):
    dist = [INF]*(V+1)
    q = []

    dist[S] = 0
    # [dist, start]
    heapq.heappush(q, [0, S])

    while q:
        now_dist, now_node = heapq.heappop(q)

        for next_node, next_weight in G[now_node]:
            next_dist = now_dist + next_weight

            if next_dist < dist[next_node]:
                dist[next_node] = next_dist
                heapq.heappush(q, [next_dist, next_node])

    return dist



V, E = map(int, readline().split())
S = int(readline())
G = [[] for _ in range(V+1)]
for _ in range(E):
    start, end, weight = map(int, readline().split())
    G[start].append([end, weight])

dist = get_shortest_dist(G, V, S)

for i in range(1, V+1):
    print(dist[i] if dist[i] < INF else 'INF')