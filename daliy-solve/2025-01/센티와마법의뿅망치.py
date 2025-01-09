# https://www.acmicpc.net/problem/19638

import heapq


N, H, T = map(int, input().split())
q = []

for _ in range(N):
    heapq.heappush(q, -int(input()))

cnt = 0

for _ in range(T):
    if -q[0] < H or -q[0] == 1:
        break
    else:
        giant = -heapq.heappop(q)
        giant = int(giant / 2) if giant >= 2 else 1 # 1 보다 작아질 수 없다
        heapq.heappush(q, -giant)
        cnt += 1

if -q[0] < H:
    print("YES")
    print(cnt)
else:
    print("NO")
    print(-q[0])