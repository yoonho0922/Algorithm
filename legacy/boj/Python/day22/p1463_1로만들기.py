from collections import deque
import sys
readline = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    count = -1

    while q:
        count += 1
        for i in range(len(q)):
            cur = q.popleft()
            if cur == 1:
                return count
            elif cur > 1:
                if cur % 3 == 0:
                    q.append(cur//3)
                if cur % 2 == 0:
                    q.append(cur//2)
                q.append(cur - 1)

N = int(readline())
print(bfs(N))