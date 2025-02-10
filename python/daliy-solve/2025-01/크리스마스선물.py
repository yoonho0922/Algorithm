# https://www.acmicpc.net/problem/14235

import heapq

N = int(input())
q = []

for _ in range(N):
    presents = list(map(int, input().split()))

    if presents[0] == 0:
        if q:
            print(-heapq.heappop(q))
        else:
            print(-1)
    else:
        for present in presents[1:]:
            heapq.heappush(q, -present)
