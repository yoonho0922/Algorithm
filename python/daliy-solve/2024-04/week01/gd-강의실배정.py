# https://www.acmicpc.net/problem/11000

import heapq
import sys
readline = sys.stdin.readline


N = int(input())
T = [list(map(int,readline().split())) for _ in range(N)]

T.sort()
q = []

ans = 0
now_lecture = 0

for start, end in T:
    now_lecture += 1
    heapq.heappush(q, end)

    while q:
        if q[0] <=start:
            heapq.heappop(q)
            now_lecture -= 1
        else:
            break
    # print(start, end, now_lecture)
    ans = max(ans, now_lecture)

print(ans)