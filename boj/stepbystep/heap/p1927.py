import heapq
import sys
readline = sys.stdin.readline

N = int(readline())
q=[]

for _ in range(N):
    a = int(readline())

    if a == 0:
        if len(q)==0:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, a)