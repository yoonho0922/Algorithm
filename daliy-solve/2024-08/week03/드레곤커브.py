# https://www.acmicpc.net/problem/15685

GRID_LEN = 100
MAX_GEN = 10

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def draw(x, y, d, g):
    cy, cx, cd = y, x, d
    G[cy][cx] = True

    for direct in dg[g]:
        cd = (direct + d)%4
        cy = cy + dy[cd]
        cx = cx + dx[cd]
        G[cy][cx] = True

def get_direction_grid():
    direction_grid = [[0]]
    for i in range(1, MAX_GEN+1):
        directions = []
        for j in range(len(direction_grid[i-1])-1, -1, -1):
            directions.append((direction_grid[i-1][j]+1)%4)
        direction_grid.append(direction_grid[i-1] + directions)
    return direction_grid



# main
N = int(input())
G = [[False]*(GRID_LEN+1) for _ in range(GRID_LEN+1)]
dg = get_direction_grid()
ans = 0

for _ in range(N):
    x, y, d, g = map(int, input().split())
    draw(x, y, d, g)

for i in range(GRID_LEN):
    for j in range(GRID_LEN):
        if G[i][j] and G[i][j+1] and G[i+1][j] and G[i+1][j+1]:
            ans += 1

print(ans)
