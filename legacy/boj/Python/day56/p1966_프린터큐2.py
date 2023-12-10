from collections import deque

def impl():
    cnt = 0

    while q:

        if q[0] == max(q):
            if idx[0] == M:
                return cnt+1

            q.popleft()
            idx.popleft()
            cnt += 1
        else:
            q.append(q.popleft())
            idx.append(idx.popleft())

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    q = deque(list(map(int, input().split())))
    idx = deque(list(range(N)))

    print(impl())