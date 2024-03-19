# https://www.acmicpc.net/problem/14499

import sys
readline = sys.stdin.readline

dy = [0,0,-1,1]
dx = [1,-1,0,0]


def rotate(graph, dice, direct, y, x):
    # direct 에 따라 주사위 굴리기
    if direct == 1:
        # 동
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
        # print('d', dice)
    if direct == 2:
        # 서
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
        # print('d', dice)
    if direct == 3:
        # 북
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
        # print('d', dice)
    if direct == 4:
        # 남
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
        # print('d', dice)


    # 주사위 업데이트
    if graph[y][x] == 0:
        # 칸 업데이트: 주사위 바닥면의 수 복사
        graph[y][x] = dice[5]
    else:
        # 칸의 수가 주사위 바닥면으로 복사, 칸의 수는 0으로 바뀜
        dice[5] = graph[y][x]
        graph[y][x] = 0

    # 주사위 상단의 수
    return dice[0]

N, M, cy, cx,K = map(int, readline().split())
G = [list(map(int, readline().split())) for _ in range(N)]
dice = [0 for _ in range(6)]


for cmd in list(map(int, readline().split())):
    # print('d cmd', cmd)
    ny = cy + dy[cmd-1]
    nx = cx + dx[cmd-1]

    if 0<=ny<N and 0<=nx<M:
        # 주사위 이동
        cy = ny
        cx = nx

        # 주사위 굴리기
        result = rotate(G, dice, cmd, ny, nx)
        print(result)