from collections import deque
import sys
readline = sys.stdin.readline

N, M, V = map(int, readline().split())
G = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, readline().split())
    G[a][b] = 1
    G[b][a] = 1

dfs_visited = [False] * (N+1)
def dfs(cur):
    print(cur, end=' ')
    dfs_visited[cur] = True
    for next in range(N+1):
        if G[cur][next] == 1 and not dfs_visited[next]:
            dfs(next)

def bfs(start):
    q = deque()
    visited = [False]*(N+1)
    q.append(start)
    visited[start] = True

    while q:
        cur = q.popleft()
        print(cur, end=' ')
        for next in range(N+1):
            if G[cur][next] == 1 and not visited[next]:
                q.append(next)
                visited[next] = True

dfs(V)
print()
bfs(V)