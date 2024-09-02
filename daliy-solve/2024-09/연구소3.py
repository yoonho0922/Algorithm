# https://www.acmicpc.net/problem/17142

from collections import deque

MAX_TIME = 1e9
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def simulate(activated):
    q = deque()
    visited = [[False] * N for _ in range(N)]
    spread_cnt = 0

    for y, x in activated:
        q.append([y, x])
        visited[y][x] = True

    time = -1

    while q:
        time += 1
        for _ in range(len(q)):
            cy, cx = q.popleft()
            for i in range(4):
                ny = cy + dy[i]
                nx = cx + dx[i]
                if 0<=ny<N and 0<=nx<N and not visited[ny][nx] and G[ny][nx] != 1:
                    q.append([ny, nx])
                    visited[ny][nx] = True
                    if G[ny][nx] == 0:
                        spread_cnt += 1
        if spread_cnt == target_cnt:
            return time

    return MAX_TIME


def dfs(activated, start):
    if len(activated) == M:
        global ans
        res = simulate(activated)
        if res < MAX_TIME:
            ans  = min(ans, res)
        return

    for i in range(start, len(virus)):
        activated.append(virus[i])
        dfs(activated, i + 1)
        activated.pop()


N, M = map(int, input().split())
G = []
virus = []
target_cnt = 0
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 2:
            virus.append([i,j])
        elif row[j] == 0:
            target_cnt += 1
    G.append(row)


ans = MAX_TIME
dfs([], 0 )
# print(simulate([[0, 0], [1, 5], [4, 3]]))
if ans < MAX_TIME:
    print(ans)
else:
    print(-1)