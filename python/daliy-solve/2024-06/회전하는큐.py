# https://www.acmicpc.net/problem/1021

from collections import deque

N, M = map(int, input().split())

q = deque(range(1, N+1))
ans = 0

for x in list(map(int,input().split())):
    # print(q)
    if q.index(x) > len(q)//2:
        # print('R', len(q) - q.index(x) - 1)
        for _ in range(len(q) - q.index(x) - 1):
            tmp = q.pop()
            q.appendleft(tmp)
            ans += 1
        q.pop()
        ans += 1
    else:
        # print('L', q.index(x))
        for _ in range(q.index(x)):
            tmp = q.popleft()
            q.append(tmp)
            ans += 1 ;

print(ans)

s = set()