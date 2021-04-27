from collections import deque

def impl():
    cnt = 0

    while q:
        if q[0] == -1:
            for i in range(len(q)):
                if priority < q[i]:
                    q.append(q.popleft())
                    break
            else:
                return cnt+1
        else:
            for i in range(len(q)):

                if q[0] < q[i] or q[0] < priority:
                    q.append(q.popleft())
                    break
            else:
                q.popleft()
                cnt += 1

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    q = deque(nums)

    priority = q[M]
    q[M] = -1

    print(impl())

