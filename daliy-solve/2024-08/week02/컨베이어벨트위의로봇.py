# https://www.acmicpc.net/problem/20055

from collections import deque


def rotate(belt, robots):
    belt.appendleft(belt.pop())
    robots.appendleft(robots.pop())


def delivery(robots):
    robots[N-1] = False

def move_robots(belt, robots):
    # 로봇 이동 직전에 로봇 내리기를 수행했으므로 belt의 N-1 칸은 항상 빈 칸이다
    # 따라서 N-2번 째 로봇 부터 이동하면 된다
    for i in range(N, 0, -1):
        if robots[i-1] and belt[i] > 0 and not robots[i]:
            robots[i-1], robots[i] = False, True
            belt[i] -= 1

def insert(belt, robots):
    if not robots[0] and belt[0] > 0:
        robots[0] = True
        belt[0] -= 1


def count_zero(belt):
    cnt = 0
    for a in belt:
        if a == 0:
            cnt += 1
    return cnt


# main
N, K = map(int, input().split())
belt = deque(map(int, input().split()))
R = 2 * N
robots = deque([False] * R)
step = 0

# 1. 컨베이어 벨트, 로봇 회전 + 로봇 내리기
# 2. 로봇 이동 + 로봇 내리기
# 3. 로봇 올리기
# 4. 내구도 확인
while count_zero(belt) < K:
    # print(step,'init', belt)
    # print(step,'init', robots)

    rotate(belt, robots)
    delivery(robots)

    # print(step,'after rotate', belt)
    # print(step,'after rotate', robots)

    move_robots(belt, robots)
    delivery(robots)
    insert(belt, robots)

    # print(step,'after move', belt)
    # print(step,'after move', robots)
    step += 1


print(step)