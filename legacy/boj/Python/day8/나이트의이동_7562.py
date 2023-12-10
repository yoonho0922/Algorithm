from collections import deque
import sys
readl = sys.stdin.readline

def bfs(s, e):

    dy = [1,1,2,2,-1,-1,-2,-2]
    dx = [2,-2,1,-1,2,-2,1,-1]

    num, q = -1, deque()
    q.append(s)
    G[s[0]][s[1]] = 1

    while q:

        for _ in range(len(q)):
            cy, cx = q.popleft()

            # 목적지에 도달하면
            if [cy, cx] == e:
                num += 1
                return num

            for i in range(8):
                ny = cy + dy[i]
                nx = cx + dx[i]

                if 0<=ny<N and 0<=nx<N and G[ny][nx] == 0:
                    q.append([ny,nx])
                    G[ny][nx] = 1

        num += 1

    return -1

# 입력
T = int(readl())

for _ in range(T):
    N = int(readl())
    G = [[0]*N for _ in range(N)]
    s = list(map(int, readl().split()))
    e = list(map(int, readl().split()))

    print(bfs(s, e))