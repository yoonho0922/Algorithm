from collections import deque
import heapq
import sys
readline = sys.stdin.readline

INF = 1e9

def pop_cans():
    prev = -INF

    while q:
        dummy = heapq.heappop(q)
        x = dummy.popleft()

        # print('x', x)

        if x < prev:
            return False
        else:
            prev = x
            if dummy:
                heapq.heappush(q, dummy)

    return True

N, K = map(int, input().split())
q = []
for _ in range(K):
    M = int(readline())
    dummy = deque(-x for x in list(map(int, input().split())))

    heapq.heappush(q, dummy)

if pop_cans():
    print('SUCCESS')
else:
    print('FAIL')