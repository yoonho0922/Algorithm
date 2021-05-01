from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        cur = q.popleft()
        for next in range(N+1):
            if not visited[next] and G[cur][next]:
                visited[next] = 1
                q.append(next)

N, M = map(int, input().split())
G = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a][b] = 1
    G[b][a] = 1

cnt = 0
visited = [0]*(N+1)
for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)