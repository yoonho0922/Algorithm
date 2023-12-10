import sys
from collections import deque
## input
M, N = map(int, input().split())
box, queue = [], deque()
for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        if line[j] == 1:
            queue.append([i,j]) # [y, x]
    box.append(line)

def bfs():

    day = -1
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while queue:
        day += 1
        # 하루동안 익은 모든 토마토 확인
        for _ in range(len(queue)):
            cy, cx = queue.popleft()
            # 상하좌우 탐색
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]

                if (0<=ny<N) and (0<=nx<M) and (box[ny][nx] == 0):
                    box[ny][nx] = box[cy][cx] + 1
                    queue.append([ny,nx])
    # 악익은 토마토 확인
    for i in box:
        if 0 in i:
            return -1

    return day

print(bfs())
