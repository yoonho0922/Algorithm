def bfs(s):
    dy = [1,-1,0,0]
    dx = [0,0,-1,1]

    q, dist = [], [[0]*M for _ in range(N)]
    dist[s[0]][s[1]] = 1
    q.append(s)

    while q:
        curr = q.pop(0)
        # curr의 상하좌우 검사
        for i in range(4):
            ny = curr[0] + dy[i]
            nx = curr[1] + dx[i]
            # next 가 범위 내에 있다면
            if 0 <= ny < N and 0 <= nx < M:
                # ny,nx 가 이동할 수 있고 방문하지 않았다면(거리가 0)
                if G[ny][nx] == 1 and dist[ny][nx] == 0:
                    dist[ny][nx] = dist[curr[0]][curr[1]] + 1
                    q.append([ny, nx])

    return dist[N-1][M-1]

# 입력
N, M = map(int, input().split())
G = [[0]*M for _ in range(N)]
for i in range(N):
    line = input()
    for j in range(M):
        G[i][j] = int(line[j])

print(bfs([0,0])) # [y,x]
