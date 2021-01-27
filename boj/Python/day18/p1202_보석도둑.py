import heapq
import sys
readline = sys.stdin.readline

N, K = map(int, readline().split())
gems = []
bags = []
for _ in range(N):
    m, v = map(int, readline().split())
    gems.append((m, v))
for _ in range(K):
    bags.append(int(readline()))

gems.sort()
bags.sort()
q = []
result = 0

i = 0
for bag in bags:

    while i < N and gems[i][0] <= bag:
        heapq.heappush(q, -gems[i][1])
        i += 1

    if q:
        result += -heapq.heappop(q)

print(result)