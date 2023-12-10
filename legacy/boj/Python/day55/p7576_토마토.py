from collections import deque

def bfs():
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    ans = -1
    while q:
        for _ in range(len(q)):
            cy, cx = q.popleft()
            for i in range(4):
                ny = cy + dy[i]
                nx = cx + dx[i]
                if 0<=ny<N and 0<=nx<M and G[ny][nx] == 0:
                    q.append([ny, nx])
                    G[ny][nx] = 1
        ans += 1
    return ans

def check(ans):
    for line in G:
        if 0 in line:
            print(-1)
            return
    print(ans)

M, N = map(int, input().split())
G = []
q = deque()
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if line[j] == 1:
            q.append([i,j])
    G.append(line)

ans = bfs()
check(ans)