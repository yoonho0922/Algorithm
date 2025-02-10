# https://www.acmicpc.net/problem/1325

from collections import deque


def bfs(start):
    cnt = 0
    q = deque()
    visited = [False] * (N+1)

    q.append(start)
    visited[start] = True

    while q:
        now = q.popleft()
        for next in G[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = True
                cnt += 1
    return cnt


N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[b].append(a)

max_connected = 0
ans = []

for i in range(1, N+1):
    result = bfs(i)
    if result > max_connected:
        max_connected = result
        ans = [i]
    elif result == max_connected:
        ans.append(i)

print(*ans)