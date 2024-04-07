# https://www.acmicpc.net/problem/11286

import heapq
import sys
readline = sys.stdin.readline

N = int(input())
q = []

for _ in range(N):
    x = int(readline())
    if x == 0:
        if q:
            number, sign = heapq.heappop(q)
            print(number * sign)
        else:
            print(0)
    if x < 0:
        heapq.heappush(q, [-1 * x, -1])
    if x > 0:
        heapq.heappush(q, [x, 1])

    # print(q)
