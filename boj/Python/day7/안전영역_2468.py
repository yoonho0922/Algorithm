from collections import deque
import sys
readl = sys.stdin.readline

def bfs(s):
    dy = [1,-1,0,0]
    dx = [0,0,-1,1]

    q = deque()
    q.append(s)
    G[s[0]][s[1]] = 0

    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if (0<=ny<N) and (0<=nx<N) and G[ny][nx] == 1:
                q.append([ny,nx])
                G[ny][nx] = 0

# 입력
N = int(readl());
matrix = [[0]*N for _ in range(N)]
for i in range(N):
    l = list(map(int, input().split()))
    for j in range(N):
        matrix[i][j] = l[j]

# 해결
max_area = 0
# 잠기는 높이가 1~99 일때 안전한 영역 검사
for i in range(0, 101):
    G = [[0]*N for _ in range(N)]

    # 안전한 지역 검사
    for j in range(N):
        for k in range(N):
            # 안전한 지역이라면
            if matrix[j][k] > i:
                G[j][k] = 1

    # 영역 검사
    area = 0
    for j in range(N):
        for k in range(N):
            # 안전한 지역이라면
            if G[j][k] == 1:
                bfs([j, k])
                area += 1

    max_area = max(max_area, area)

print(max_area)