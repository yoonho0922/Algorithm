# 이코테 p.259
# 미래도시

import sys
readline = sys.stdin.readline
INF = int(1e9)


N, M = map(int, readline().split())
graph = [[INF]*(N+1) for _ in range(N+1)]

# 자기 자신에 대한 경로 초기화
for i in range(N):
    graph[i][i] = 0

# 연결된 경로 초기화
for _ in range(M):
    a, b = map(int, readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

# N 개의 노드에 해대 점화식 수행
for mid in range(1, N+1):
    for start in range(1, N+1):
        for end in range(1, N+1):
            graph[start][end] = min(graph[start][end], graph[start][mid] + graph[mid][end])

X, K = map(int, readline().split())

dist = graph[1][K] + graph[K][X]

if dist < INF:
    print(dist)
else:
    print(-1)