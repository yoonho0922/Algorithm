# https://www.acmicpc.net/problem/1913

from collections import deque

# 하, 우, 상, 좌
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


N = int(input()) # 3이상 999 이하의 홀수
num = int(input()) # N^2 이하의

grid = [[-1] * N for _ in range(N)]

q = deque()
grid[0][0] = N * N
q.append([0, 0])
direction = 0

position = []

while q:
    cy, cx = q.popleft()
    cur_num = grid[cy][cx]

    if cur_num == num:
        position = [cy + 1, cx + 1]

    for i in range(2):
        direction = (direction + i) % 4
        ny = cy + dy[direction]
        nx = cx + dx[direction]

        if 0 <= ny < N and 0 <= nx < N and grid[ny][nx] == -1:
            grid[ny][nx] = cur_num - 1
            q.append([ny, nx])
            break

for row in grid:
    print(*row)

print(*position)