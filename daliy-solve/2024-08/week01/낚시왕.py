# https://www.acmicpc.net/problem/17143


UP, DOWN, RIGHT, LEFT = 1, 2, 3, 4

# 나머지 연산이 있으면 0부터 시작하는게 좋다
def move(y, x, speed, direct):
    if speed == 0:
        return y, x, direct

    # 방향이 위쪽, 아래쪽
    if direct in [UP, DOWN]:
        cycle = 2 * (R - 1)
        if direct == UP:
            speed += cycle - y
        else:
            speed += y

        ny = speed % cycle
        if ny >= R:
            return [cycle - ny, x, UP]
        return [ny, x, DOWN]
    # 방향이 오른쪽, 왼쪽
    else:
        cycle = 2 * (C - 1)
        if direct == LEFT:
            speed += cycle - x
        else:
            speed += x

        nx = speed % cycle
        if nx >= C:
            return [y, cycle - nx, LEFT]
        return [y, nx, RIGHT]


# main
R, C, M = map(int, input().split())
G = [[-1]*C for _ in range(R)]
sharks = []
for i in range(M):
    y, x, s, d, z = map(int, input().split())
    G[y-1][x-1] = i
    sharks.append([s,d,z]) # 속력, 방향, 크기

ans = 0

# 낚시왕의 이동
for col in range(C):
    # 1. col 열의 상어를 모두 잡는다
    for row in range(R):
        if G[row][col] != -1:
            ans += sharks[G[row][col]][2]
            G[row][col] = -1
            break

    # 이동 후 상어 배치
    new_G = [[-1]*C for _ in range(R)]

    # 2. 상어가 이동한다
    for i in range(R):
        for j in range(C):
            now = G[i][j]
            if now == -1:
                continue

            s, d, z = sharks[now]
            new_r, new_c, new_d = move(i, j, s, d)
            sharks[now][1] = new_d

            # 기존의 상어가 존재하면 크기를 비교하고 제거 후 배치 결정
            if new_G[new_r][new_c] != -1:
                existed = new_G[new_r][new_c]
                existed_size = sharks[existed][2]
                if existed_size < z:
                    new_G[new_r][new_c] = now
            # 빈 공간이라면 상어 배치
            else:
                new_G[new_r][new_c] = now

    G = new_G

print(ans)