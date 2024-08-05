# https://www.acmicpc.net/problem/15683

# 1. cameras 방향에 대해 backtracking
# 2. 회전하며 카메라 시야 밝히기
# 3. depth 끝에 도달했을 때 grid 복사 및 방향에 따른 시야 검사

MAX_AREA=8*8
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]


def see_straight(grid, y, x, direct):
    ny, nx = y, x
    while 0 <= ny < N and 0 <= nx < M:
        if grid[ny][nx] == 0:
            grid[ny][nx] = 9
        elif grid[ny][nx] == 6:
            break
        ny += dy[direct]
        nx += dx[direct]


def check_vision(directions):
    grid = [r[:] for r in G]

    for c in range(K):
        y, x, type = cameras[c]
        direct = directions[c]

        if type == 1:
            see_straight(grid, y, x, direct)
        elif type == 2:
            see_straight(grid, y, x, direct)
            see_straight(grid, y, x, (direct+2)%4)
        elif type == 3:
            see_straight(grid, y, x, direct)
            see_straight(grid, y, x, (direct+1)%4)
        elif type == 4:
            see_straight(grid, y, x, direct)
            see_straight(grid, y, x, (direct+1)%4)
            see_straight(grid, y, x, (direct+2)%4)
        elif type == 5:
            see_straight(grid, y, x, direct)
            see_straight(grid, y, x, (direct+1)%4)
            see_straight(grid, y, x, (direct+2)%4)
            see_straight(grid, y, x, (direct+3)%4)
        else:
            raise Exception()

    invisible = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                invisible += 1

    return invisible


def backtrack(directions, depth):
    if depth == K:
        global ans
        invisible = check_vision(directions)
        ans = min(ans, invisible)
        return

    for direct in range(4):
        backtrack(directions + [direct], depth + 1)


N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]

cameras = [] # y, x, type
for i in range(N):
    for j in range(M):
        if 1<=G[i][j]<=5:
            cameras.append([i, j, G[i][j]])
K = len(cameras)

ans = MAX_AREA
backtrack([], 0)
print(ans)