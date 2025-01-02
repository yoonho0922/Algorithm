# https://www.acmicpc.net/problem/13335

from collections import deque

N, W, L = map(int, input().split())
trucks = list(map(int, input().split()))

q = deque([0] * W)
time = 0
target = 0 # 다음에 나갈 트럭, 최대 N - 1

while target < N:
    q.popleft()
    if (sum(q) + trucks[target]) <= L:
        q.append(trucks[target])
        target += 1
    else:
        q.append(0)
    time += 1

time += W # 마지막 트럭이 다리를 지나는 시간

print(time)