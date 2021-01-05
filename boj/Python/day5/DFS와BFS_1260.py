from collections import deque
import sys
input = sys.stdin.readline

def dfs(curr):

    visited.append(curr)
    # 모든 노드 방문
    for next in range(N+1):
        # curr 과 연결되어 있고 방문하지 않았다면
        if G[curr][next] == 1 and next not in visited:
            # 방문
            dfs(next)

def bfs(s):

    q = [s]
    visited.append(s)

    while q:
        curr = q.pop(0)
        # 모든 노드 방문
        for next in range(N+1):
            # curr 과 연결되어 있고 방문하지 안았다면
            if G[curr][next] == 1 and next not in visited:
                visited.append(next)
                q.append(next)


# 입력
N, M, V = map(int, input().split())
G = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    line = list(map(int, input().split()))
    G[line[0]][line[1]] = 1
    G[line[1]][line[0]] = 1

visited = []
dfs(V)
print(*visited)

visited = []
bfs(V)
print(*visited)
