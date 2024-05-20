from collections import deque
import sys
readline = sys.stdin.readline

N, M = map(int, input().split())
q = deque()
now_weight = 0
max_weight = 0

for _ in range(N):
    A = int(readline())

    if len(q) < M:
        now_weight += A
        q.append(A)
    elif len(q) == M:
        now_weight -= q.popleft()
        now_weight += A
        q.append(A)

    # print(now_weight, q)
    max_weight = max(max_weight, now_weight)

print(max_weight)