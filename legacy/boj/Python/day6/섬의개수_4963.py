from collections import deque
import sys
readl = sys.stdin.readline

def bfs(s):
    dy = [1,-1,0,0,-1,-1,1,1]
    dx = [0,0,-1,1,1,-1,-1,1]
    q = deque()
    q.append(s)
    G[s[0]][s[1]] = 0
    while q:
        cy, cx = q.popleft()
        for i in range(8):
            ny = cy + dy[i]
            nx = cx + dx[i]
            # 범위 안에 있고 방문하지 않았다면
            if 0<=ny<H and 0<=nx<W and G[ny][nx] == 1:
                q.append([ny,nx])
                G[ny][nx] = 0

while True:
    W, H = map(int, readl().split())
    if W == 0 and H == 0: break

    G = [[0]*W for _ in range(H)]
    for i in range(H):
        l = list(map(int, readl().split()))
        for j in range(W):
            G[i][j] = l[j]
    # 해결
    total = 0
    for i in range(H):
        for j in range(W):
            if G[i][j] == 1:
                bfs([i,j])
                total += 1
    print(total)