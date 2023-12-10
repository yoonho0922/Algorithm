from collections import deque

N = int(input())
M = int(input())
G = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a][b] = 1
    G[b][a] = 1

def search(start):
    visited = [0] * (N+1)
    q = deque()
    q.append(start)
    visited[start] = 1
    ans = 0
    while q:
        cur = q.popleft()
        for i in range(N+1):
            if G[cur][i] and not visited[i]:
                q.append(i)
                visited[i] = 1
                ans += 1
    return ans

print(search(1))