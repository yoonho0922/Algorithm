# https://www.acmicpc.net/problem/14500

import sys
readline = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


# ㅜ 모양 탐색
def get_max_exception_case(y, x):
    global max_total

    # 중심 주변 값 조사
    sides = []
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0<=ny<N and 0<=nx<M:
            sides.append(G[ny][nx])

    # 주변값이 3개 이상일 경우 모양을 만들 수 있음
    if len(sides) >=3:
        # print('d i,j', y,x)
        # print('d sides', sides)
        # 주변 값 중 가장 큰 3개 값을 중심값과 더함
        tops = sorted(sides, reverse=True)[:3]
        # print('d tops', tops)
        total = G[y][x] + sum(tops)
        max_total = max(max_total, total)


def get_max_normal_case(depth, y, x, total):
    global max_total

    if depth == 4:
        max_total = max(max_total, total)
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0<=ny<N and 0<=nx<M and not visited[ny][nx]:
            visited[ny][nx]=True
            get_max_normal_case(depth + 1, ny, nx, total + G[y][x])
            visited[ny][nx]=False

N, M = map(int, input().split())
G = [list(map(int, readline().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

max_total = 0

for i in range(N):
    for j in range(M):
        visited[i][j]=True
        get_max_normal_case(0, i, j, 0)
        visited[i][j]=False

        get_max_exception_case(i, j)

print(max_total)