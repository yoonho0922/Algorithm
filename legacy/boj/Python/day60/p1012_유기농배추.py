from collections import deque

def bfs(start):
    dy = [0,0,-1,1]
    dx = [1,-1,0,0]
    q = deque()
    q.append(start)
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<N and 0<=nx<M and G[ny][nx]:
                q.append([ny,nx])
                G[ny][nx] = 0

def search():
    cnt = 0

    for i in range(M):
        for j in range(N):
            if G[j][i]:
                cnt += 1
                bfs([j, i])

    print(cnt)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    G = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        G[y][x] = 1
    search()
