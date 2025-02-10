# https://www.acmicpc.net/problem/2573

# 1. 녹이기
# 2. BFS 로 분할 체크
# 3. 1로 반복

from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

# 바다에 닿은 면의 갯수 구하기
def count_sea(r, c):
    cnt = 0
    for i in range(4):
        ny = r + dy[i]
        nx = c + dx[i]
        if 0<=ny<N and 0<=nx<M and G[ny][nx] == 0:
            cnt += 1
    return cnt

# 빙하가 녹으면 True, 녹일 빙하가 없으면 False 반환
def melt():
    global G
    melted = False
    next_G = [[0]*M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if G[r][c] != 0:
                cnt = count_sea(r, c)
                next_G[r][c] = max(G[r][c] - cnt, 0)
                melted = True
    G = next_G
    return melted

def bfs(r: int, c: int, visited):
    q = deque()
    visited[r][c] = True
    q.append((r,c))
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<N and 0<=nx<M and G[ny][nx] != 0and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx))
    return



N, M = map(int, input().split())
G = []
for _ in range(N):
    G.append(list(map(int, input().split())))

year = 0

while melt():
    year += 1
    visited = [[False]*M for _ in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(M):
            if G[r][c] != 0 and not visited[r][c]:
                bfs(r, c, visited)
                cnt += 1
    if cnt > 1:
        print(year)
        break
else:
    print(0)