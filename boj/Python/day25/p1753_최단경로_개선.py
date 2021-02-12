import heapq
import sys
readline = sys.stdin.readline
INF = 100000000

N, M = map(int, readline().split())
start = int(readline())

graph = [[] for _ in range(N + 1)]
distance = [INF] * (N+1)

for _ in range(M):
    a, b, c = map(int, readline().split())
    # a 노드 -> b 노드 : 비용 c
    graph[a].append((b, c))

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        cur_dist, cur_v = heapq.heappop(q)

        # 현재 노드오 연결된 다른 노드들 확인
        for v, w in graph[cur_v]:
            cost = cur_dist + w
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧으면 갱신
            if cost < distance[v]:
                distance[v] = cost
                # 갱신한 노드를 힙에 푸시
                heapq.heappush(q, (cost, v))

dijkstra(start)

for i in distance[1:]:
    print(i if i != INF else 'INF')