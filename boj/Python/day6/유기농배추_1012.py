from sys import stdin
from collections import deque

def bfs(s):
    dy = [1,-1,0,0]
    dx = [0,0,-1,1]

    q = deque()
    q.append(s)
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            # 범위를 넘지 않고 방문하지 않았다면
            if 0<=ny<N and 0<=nx<M and G[ny][nx] == 1:
                G[ny][nx] =0
                q.append([ny,nx])


T = int(stdin.readline())
for _ in range(T):
    # 입력
    M, N, K = map(int, input().split())
    G = [[0]*M for _ in range(N)]
    for _ in range(K):
        l = list(map(int, input().split()))
        G[l[1]][l[0]] = 1 # y, x
    # 해결
    total = 0 # 필요한 지렁이의 수
    for i in range(N):
        for j in range(M):
            if G[i][j] == 1:
                bfs([i, j])
                total += 1
    print(total)