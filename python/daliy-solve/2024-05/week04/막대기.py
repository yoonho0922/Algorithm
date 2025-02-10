# https://www.acmicpc.net/problem/1094

import heapq

X = int(input())

q = [64]

while sum(q)>X:
    x = heapq.heappop(q)
    heapq.heappush(q, x//2)

    if not (sum(q) >= X):
        heapq.heappush(q, x//2)

print(len(q))