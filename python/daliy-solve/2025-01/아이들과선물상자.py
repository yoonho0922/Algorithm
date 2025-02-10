# https://www.acmicpc.net/problem/23757

import heapq

N, M = map(int, input().split())
q = []

for present in list(map(int, input().split())):
    heapq.heappush(q, -present)

for c in list(map(int, input().split())):
    present = -heapq.heappop(q)
    if present >= c:
        remained = present - c
        heapq.heappush(q, -remained)
    else:
        print(0)
        break
else:
    print(1)