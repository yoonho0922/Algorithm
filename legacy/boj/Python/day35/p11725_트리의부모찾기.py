from collections import deque
import sys
readline = sys.stdin.readline

def bfs(start):
    q = deque()
    visited = [False] * (N+1)

    q.append(start)
    visited[start] = True

    while q:
        cur = q.popleft()

        for next in G[cur]:
            if visited[next]:
                continue
            answer[next] = cur
            q.append(next)
            visited[next] = True


N = int(readline())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, readline().split())
    G[a].append(b)
    G[b].append(a)

answer = [0]*(N+1)
bfs(1)

for i in range(2, N+1):
    print(answer[i])