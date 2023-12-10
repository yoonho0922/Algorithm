from collections import deque
import sys
readline = sys.stdin.readline

def bfs(s, e):
    q = deque()
    q.append(s)
    res = 0
    while q:

        for _ in range(len(q)):
            cur = q.popleft()

            if cur == e:
                print(res+1)
                return

            for next in [cur * 2, cur * 10 + 1]:

                if next <= e:
                    q.append(next)

        res += 1

    print(-1)

A, B = map(int, readline().split())

bfs(A, B)