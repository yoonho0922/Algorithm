# https://www.acmicpc.net/problem/10845

import sys
from collections import deque
readline = sys.stdin.readline

N = int(input())
q = deque()

for _ in range(N):
    row = list(readline().rstrip().split())

    if row[0] == 'push':
        q.append(row[1])
    if row[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    if row[0] == 'size':
        print(len(q))
    if row[0] == 'empty':
        print(int(len(q)==0))
    if row[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    if row[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)