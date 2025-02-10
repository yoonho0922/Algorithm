# https://www.acmicpc.net/problem/10866

import sys
import collections
readline = sys.stdin.readline

N = int(input())

q = collections.deque()

for _ in range(N):
    cmd = readline().split()

    if 'push_front' == cmd[0]:
        x = cmd[1]
        q.appendleft(x)
    if 'push_back' == cmd[0]:
        x = cmd[1]
        q.append(x)
    if 'pop_front' == cmd[0]:
        if q:
            print(q.popleft())
        else:
            print(-1)
    if 'pop_back' == cmd[0]:
        if q:
            print(q.pop())
        else:
            print(-1)
    if 'size' == cmd[0]:
        print(len(q))
    if 'empty' == cmd[0]:
        if not q:
            print(1)
        else:
            print(0)
    if 'front' == cmd[0]:
        if q:
            print(q[0])
        else:
            print(-1)
    if 'back' == cmd[0]:
        if q:
            print(q[-1])
        else:
            print(-1)
