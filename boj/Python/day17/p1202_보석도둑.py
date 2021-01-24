import heapq
import sys
readline = sys.stdin.readline

N, K = map(int, readline().split())
gems, bags = [], []
for _ in range(N):
    m, v = map(int, readline().split())
    gems.append((m, v))
for _ in range(K):
    bags.append(int(readline()))

gems.sort()
bags.sort()

max_heap = []
result = 0
j = 0

for i in range(K):

    while j<N and gems[j][0] <= bags[i]:
        heapq.heappush(max_heap, -gems[j][1])
        j += 1

    if max_heap:
        v = heapq.heappop(max_heap)
        result += abs(v)

print(result)