from collections import deque
import sys
readl = sys.stdin.readline

def bfs(s):
    dy = [1,-1,0,0]
    dx = [0,0,-1,1]

    q = deque()
    q.append(s)
    G[s[0]][s[1]] = 1
    area = 1

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<M and 0<=nx<N and G[ny][nx] == 0:
                q.append([ny,nx])
                G[ny][nx] = 1
                area += 1
    return area

M, N, K = map(int, readl().split())
G = [[0]*N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            G[i][j] = 1

# 해결
total = 0
areas = []
for i in range(M):
    for j in range(N):
        # 색칠되지 않은 영역이라면
        if G[i][j] == 0:
            areas.append(bfs([i, j]))
            total += 1

areas.sort()

print(total)
for a in areas:
    print(a, end=' ')