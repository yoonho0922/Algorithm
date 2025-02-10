# https://www.acmicpc.net/problem/17144

# 우, 상, 좌, 하
dY = [0,-1,0,1]
dX = [1, 0, -1, 0]

def spread(G, spread_area, cY, cX, amount):
    cnt = 0
    for i in range(4):
        nY = cY + dY[i]
        nX = cX + dX[i]

        if 0<=nY<R and 0<=nX<C and G[nY][nX] != -1:
            cnt += 1
            spread_area[nY][nX] += amount

    return cnt

def spread_all(G):
    spread_area = [[0]*C for _ in range(R)]

    for y in range(R):
        for x in range(C):
            if G[y][x] > 0:
                amount = G[y][x] // 5
                added_cnt = spread(G, spread_area, y, x, amount)
                G[y][x] -= amount * added_cnt

    for y in range(R):
        for x in range(C):
            if G[y][x] != -1:
                G[y][x] += spread_area[y][x]


def clean(row, G):
    cY, cX = row, 1
    direct = 0 # 우>상>좌>하
    prev = 0

    while [cY, cX] != [row, 0]:
        G[cY][cX], prev = prev, G[cY][cX]

        # 현재 위치가 꼭지점이라면 방향 변경
        if [cY, cX] in [[0,0], [0,C-1], [row, C-1], [row, 0]]:
            direct += 1
            if direct >4:
                raise Exception()

        cY = cY + dY[direct]
        cX = cX + dX[direct]


def check_air(G):
    ans = 0
    for i in range(R):
        for j in range(C):
            if G[i][j] != -1:
                ans += G[i][j]
    return ans


# main
R, C, T = map(int, input().split())
cleaner_rows = []
G = []

for i in range(R):
    G.append(list(map(int, input().split())))
    if G[i][0] == -1:
        cleaner_rows.append(i)

if len(cleaner_rows) != 2:
    raise Exception()


# 1. 미세먼지 확산
# 2. 공기청정기 순환
# 3. T초 후 미세먼지 계산
for step in range(T):
    spread_all(G)

    clean(cleaner_rows[0], G)

    # 상하 뒤집어서 clean 후 다시 뒤집기
    rotated_G = [x[:] for x in G[::-1]]
    clean(R-1-cleaner_rows[1], rotated_G)
    G = [x[:] for x in rotated_G[::-1]]

    # print(step+1)
    # for x in G:
    #     print(x)


print(check_air(G))