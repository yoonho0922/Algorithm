from collections import deque
import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, readline().split())
    G[a].append(b)
    G[b].append(a)

def bfs(start, bacon):
    q = deque()
    distance = [0] * (N+1)
    visited = [False] * (N+1)

    q.append(start)
    visited[start] = True

    while q:
        cur = q.popleft()

        for i in range(len(G[cur])):
            next = G[cur][i]
            if visited[next]:
                continue
            visited[next] = True
            distance[next] = distance[cur] + 1
            q.append(next)

    return sum(distance)


numbers = [0] * (N+1)

for i in range(1, N+1):
    numbers[i] = bfs(i, -1)

answer = N

for i in range(N, 0, -1):
    if numbers[i] <= numbers[answer]:
        answer = i

print(answer)