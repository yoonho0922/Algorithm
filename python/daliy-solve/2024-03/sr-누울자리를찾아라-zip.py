# https://www.acmicpc.net/problem/1652

import sys

readline = sys.stdin.readline

N = int(readline())
h_place = [readline() for _ in range(N)]
# 세로 방향을 반복문 두번째 depth 에서 접근 가능하도록 회전
v_place = [''.join(x) for x in zip(*h_place)]

h_cnt, v_cnt = 0, 0

for i in range(N):
    # 가로로 누울 수 있는지 확인
    for part in h_place[i].split('X'):
        if '..' in part:
            h_cnt += 1
    # 세로로 누울 수 있는지 확인
    for part in v_place[i].split('X'):
        if '..' in part:
            v_cnt += 1

print(h_cnt, v_cnt)