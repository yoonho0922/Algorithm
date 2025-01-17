# https://www.acmicpc.net/problem/1911

import sys
readline = sys.stdin.readline

N, L = map(int, readline().split())
pools = [list(map(int, readline().split())) for _ in range(N)]
pools.sort()

answer = 0
here = pools[0][0] # 첫 번째 웅덩이 시작 지점 부터 시작

for pool in pools:
    start, end = pool[0], pool[1]
    here = max(start, here)
    gap = end - here

    if gap % L != 0:
        cnt = gap // L + 1
        answer += cnt
        here = here + cnt * L
    else:
        answer += gap // L
        here = end
    # print("info", end, here, answer)

print(answer)