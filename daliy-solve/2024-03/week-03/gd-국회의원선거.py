# https://www.acmicpc.net/problem/1417

import heapq

N = int(input())
A = int(input())
q = []

if N==1:
    print(0)
    exit()

for _ in range(N-1):
    heapq.heappush(q, -int(input()))

cnt = 0

while not(A > -q[0]):
    candi = -heapq.heappop(q)
    heapq.heappush(q, -(candi-1))
    A += 1

    cnt += 1

print(cnt)