# https://www.acmicpc.net/problem/14940

from collections import deque

dy = [1,-1,0,0]
dx = [0,0,1,-1]


def solve(sy, sx):
    dists = [[-1]*M for _ in range(N)]
    q = deque()

    q.append([sy, sx])
    dists[sy][sx] = 0

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<N and 0<=nx<M and G[ny][nx] == 1 and dists[ny][nx] == -1:
                dists[ny][nx] = dists[cy][cx] + 1
                q.append([ny,nx])

    return dists



N, M = map(int, input().split())
G = []
sy, sx = 0, 0
for i in range(N):
    G.append(list(map(int, input().split())))
    if 2 in G[i]:
        sy, sx = i, G[i].index(2)

dists = solve(sy, sx)

for i in range(N):
    for j in range(M):
        if G[i][j] == 0:
            dists[i][j] = 0
    print(*dists[i])