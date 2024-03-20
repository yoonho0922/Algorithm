# https://www.acmicpc.net/problem/3190

import sys
import collections
readline = sys.stdin.readline

# 1. 뱀 몸 위치 정보 snake 배열
# 2. 이동할 위치가 괜찮은지 체크 - 1. 벽이 아닌지, 2. 몸통이 아닌지. 안괜찮으면 끝
# 2. 이동할 위치를 snake에 append
# 3. 이동할 위치에 사과가 없다면 popleft()
# 4. O(10000 * 100)

# 동 남 서 북
dy = [0,1,0,-1]
dx = [1,0,-1,0]

# 입력
N = int(input())
K = int(input())
G = [[0]*(N+1) for _ in range(N+1)]
for _ in range(K):
    y, x = map(int, readline().split())
    G[y][x] = 1
M = int(input())
control = []
for _ in range(M):
    cmd = readline().rstrip().split()
    control.append([int(cmd[0]),cmd[1]])

# 게임 정보 초기화
time = 0
# 뱀 몸의 위치 정보 [꼬리,몸통,...,몸통,머리]
snake = collections.deque([(1,1)])
direct = 0 # 동쪽


def is_conflict(ny, nx, N):
    # 영역을 벗어나거나
    if not (1<=ny<=N and 1<=nx<=N):
        return True
    # 몸통과 부딪힌다면
    if (ny, nx) in snake:
        return True

    return False


def move_snake():
    global time

    # 시간 증가
    time += 1

    ny = snake[-1][0] + dy[direct]
    nx = snake[-1][1] + dx[direct]

    # 갈 수 있는지 확인
    if is_conflict(ny,nx, N):
        return False

    snake.append((ny,nx))

    # 이동한 곳에 먹이가 없다면 꼬리 줄이기
    if G[ny][nx] != 1:
        snake.popleft()
    # 사과가 있다면 사과 없애기
    else:
        G[ny][nx] = 0

    return True


def control_snake(t):
    for _ in range(t):
        if not move_snake():
            return False

    return True


def change_direct(d):
    global direct

    # 왼쪽으로 90도
    if d == 'L':
        direct = (direct - 1) % 4
    # 오른쪽으로 90도
    else:
        direct = (direct + 1) % 4

# ================================게임 시작 =====================================
# 최악의 경우 100 * 10,000 * 100
for t, d in control:
    # 현재 상태에서 정보 업데이트

    # 다음 명령이 나올때 까지(t-time) 뱀 이동
    completed = control_snake(t-time)

    # 이동이 온전히 진행되지 않았다면 종료
    if not completed:
        break

    # 방향 전환
    change_direct(d)

# 충돌이 안났다면 계속 진행
else:
    while True:
        if not move_snake():
            break

print(time)