from collections import deque
import sys
readl = sys.stdin.readline

def bfs():

    dh = [1,-1,0,0,0,0]
    dy = [0,0,1,-1,0,0]
    dx = [0,0,0,0,1,-1]

    day = -1

    while q:
        # 하루에 익을 수 있는 토마토 모두 검사
        for _ in range(len(q)):
            ch, cy, cx = q.popleft()
            # 여섯 방향을 검사
            for i in range(6):
                nh = ch + dh[i]
                ny = cy + dy[i]
                nx = cx + dx[i]

                if 0<=nh<H and 0<=ny<N and 0<=nx<M and G[nh][ny][nx] == 0:
                    q.append([nh,ny,nx])
                    G[nh][ny][nx] = 1

        day += 1

    return day


# 입력
M, N, H = map(int, readl().split())
G = [[[0]*M for _ in range(N)] for _ in range(H)]
q = deque()

for i in range(H):
    for j in range(N):
        line = list(map(int, readl().split()))
        for k in range(M):
            G[i][j][k] = line[k]
            # 익은 토마토라면
            if line[k] == 1:
                q.append([i, j, k]) # z, y, x

day = bfs()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if G[i][j][k] == 0:
                day = -1

print(day)