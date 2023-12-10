from sys import stdin
from collections import deque

def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 1
    while q:
        curr = q.popleft()
        for next in G[curr]:
            # 방문하지 않았다면
            if visited[next] == 0:
                q.append(next)
                visited[next] = 1
# 입력
N, M = map(int, stdin.readline().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    l = list(map(int, stdin.readline().split()))
    G[l[0]].append(l[1])
    G[l[1]].append(l[0])
# 해결
visited = [0]*(N+1)
total = 0
# 모든 노드를 검사
for i in range(1, N+1):
    # 방문하지 않았다면
    if visited[i] == 0:
        bfs(i)
        total += 1
print(total)