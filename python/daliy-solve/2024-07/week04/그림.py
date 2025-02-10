# https://www.acmicpc.net/problem/1926

from collections import deque


dY = [0,0,1,-1]
dX = [1,-1,0,0]

def bfs(sY, sX):
    q = deque()

    q.append([sY, sX])
    visited[sY][sX] = True

    area = 0

    while q:
        cY, cX = q.popleft()
        area += 1

        for i in range(4):
            nY = cY + dY[i]
            nX = cX + dX[i]

            if 0<=nY<N and 0<=nX<M and not visited[nY][nX] and G[nY][nX] == 1:
                q.append([nY,nX])
                visited[nY][nX] = True

    return area


N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

cnt, widest_area = 0, 0

for i in range(N):
    for j in range(M):
        if not visited[i][j] and G[i][j] == 1:
            area = bfs(i, j)
            widest_area = max(widest_area, area)
            cnt += 1

print(cnt)
print(widest_area)