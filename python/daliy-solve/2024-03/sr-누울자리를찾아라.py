# https://www.acmicpc.net/problem/1652

import sys
import copy
readline = sys.stdin.readline

N = int(readline())
v_place = [list(readline().rstrip()) for _ in range(N)]
h_place = copy.deepcopy(v_place)

h_cnt = 0
v_cnt = 0

for i in range(N):
    for j in range(N-1):
        # 가로로 누울자리 확인
        if h_place[i][j] == h_place[i][j+1] == '.':
            h_cnt += 1
            # 장애물을 만나기 전까지 가로로 X 처리
            for k in range(j, N):
                if h_place[i][k] == 'X':
                    break
                h_place[i][k] = 'X'

        # 세로로 누울자리 확인
        if v_place[j][i] == v_place[j+1][i] == '.':
            v_cnt += 1
            # 장애물을 만나기 전까지 세로로 X 처리
            for k in range(j, N):
                if v_place[k][i] == 'X':
                    break
                v_place[k][i] = 'X'

print(h_cnt, v_cnt)