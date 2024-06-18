# https://www.acmicpc.net/problem/1941

from collections import deque

dY = [0, 0, -1, 1]
dX = [1, -1, 0, 0]

# bfs로 위치 조합이 이어졌는지 확인
def bfs_check(s):
    q = deque()
    visited = [False] * 7

    q.append(s[0])
    visited[0] = True

    while q:
        cur = q.popleft()
        cY, cX = cur//5, cur%5
        for i in range(4):
            nY = cY + dY[i]
            nX = cX + dX[i]
            next = nY*5 + nX
            if 0<=nY<N and 0<=nX<N and next in s and not visited[s.index(next)]:
                visited[s.index(next)] = True
                q.append(next)

    return False not in visited

# 조합에서 Y의 개수
def count_y(combi):
    y = 0
    for x in combi:
        if G[x//5][x%5] == 'Y':
            y += 1
    return y

# 조합을 통해 문제 조건 검사 25C7 = 약 10^5
def dfs(visited):
    if len(visited) == 7:
        if bfs_check(visited):
            global ans
            ans += 1
        return

    # 0 ~ 24
    for i in range(visited[-1] + 1, N*N):
        if i not in visited and count_y(visited + [i]) < 4:
            dfs(visited + [i])


N = 5
G = [list(input()) for _ in range(N)]
ans = 0

# 0 ~ 24
for i in range(N*N):
    dfs([i])

print(ans)