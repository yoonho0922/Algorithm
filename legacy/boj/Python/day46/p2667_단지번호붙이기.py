from collections import deque

N = int(input())
G = []
for _ in range(N):
    G.append(list(map(int, input())))

def bfs(start):
    count = 0
    q = deque()
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    q.append(start)
    G[start[0]][start[1]] = 0
    while q:
        cy, cx = q.pop()
        count += 1
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<N and 0<=nx<N and G[ny][nx] == 1:
                q.append([ny,nx])
                G[ny][nx] = 0
    return count

ans = 0
counts = []
for i in range(N):
    for j in range(N):
        if G[i][j] == 1:
            ans += 1
            counts.append(bfs([i,j]))
counts.sort()
print(ans)
for c in counts:
    print(c)
