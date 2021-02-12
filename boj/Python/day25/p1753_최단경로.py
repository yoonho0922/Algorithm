import sys
readline = sys.stdin.readline
INF = 100

N, M = map(int, readline().split())
start = int(readline())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
distance = [INF] * (N+1)

for _ in range(M):
    a, b, c = map(int, readline().split())
    # a 노드에서 b 노드로 가능 비용이 c
    graph[a].append((b, c))

def get_smallest_node():
    min_distance = INF
    index = 0
    # 방문하지 않은 노드 중 거리가 가장 짧은 노드 선택
    for i in range(1, N + 1):
        if distance[i] < min_distance and not visited[i]:
            min_distance = distance[i]
            index = i

    return index

def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0

    # N개의 노드에 대해 반복
    for _ in range(N):
        cur = get_smallest_node()
        visited[cur] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for v, w in graph[cur]:
            cost = distance[cur] + w
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧으면 갱신
            if cost < distance[v]:
                distance[v] = cost

dijkstra(start)

for i in range(1, N + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])