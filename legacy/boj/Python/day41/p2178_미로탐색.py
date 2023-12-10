from collections import deque
import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
G = [[0]*M for _ in range(N)]
for i in range(N):
    s = readline().strip()
    for j in range(M):
        G[i][j] = int(s[j])

def bfs(start):
    q = deque()
    dy, dx = [1,-1,0,0], [0,0,-1,1]
    ans = 0
    G[start[0]][start[1]] = 0
    q.append(start)
    while q:
        ans += 1
        for _ in range(len(q)):
            cy, cx = q.popleft()
            if cy == N-1 and cx == M-1:
                return ans
            for i in range(4):
                ny = cy + dy[i]
                nx = cx + dx[i]
                if 0 <= ny < N and 0 <= nx < M and G[ny][nx] == 1:
                    G[ny][nx] = 0
                    q.append([ny, nx])

print(bfs([0,0]))