from collections import deque

def dfs(curr):
    visited[curr] = 1
    print(curr, end= ' ')
    for next in range(N+1):
        # 연결되어있고 방문하지 않았다면
        if G[curr][next] == 1 and visited[next] == 0:
            dfs(next)

def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 1
    while q:
        curr = q.popleft()
        print(curr, end=' ')
        for next in range(N+1):
            # 연결되어있고 방문하지 않았다면
            if G[curr][next] == 1 and visited[next] == 0:
                q.append(next)
                visited[next] = 1

#입력
N, M, V = map(int, input().split())
G = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    l = list(map(int, input().split()))
    G[l[0]][l[1]] = 1
    G[l[1]][l[0]] = 1

visited = [0]*(N+1)
dfs(V)
print()
visited = [0]*(N+1)
bfs(V)