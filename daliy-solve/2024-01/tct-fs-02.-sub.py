# 미로 탈출

import collections

N, M = map(int, input().split())
G = []
for _ in range(N):
    G.append(list(map(int, input())))

dy = [0,0,1,-1]
dx = [1,-1,0,0]

def bfs(start):
    q = collections.deque()
    q.append(start)

    count = 0

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy+dy[i]
            nx = cx+dx[i]
            if 0<=ny<N and 0<=nx<M and G[ny][nx]==1:
                G[ny][nx] = G[cy][cx] + 1
                q.append((ny,nx))

bfs((0,0))
print(G[N-1][M-1])