# https://www.acmicpc.net/problem/14502

import collections
import copy

def get_safe(place):
    cnt = 0

    for i in range(N):
        for j in range(M):
            if place[i][j] == 0:
                cnt += 1

    return cnt


def bfs(place):
    q = collections.deque()

    dy = [0,1,0,-1]
    dx = [1,0,-1,0]

    for y, x in virus:
        q.append((y,x))

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0<=ny<N and 0<=nx<M and place[ny][nx]==0:
                place[ny][nx] = 2
                q.append((ny,nx))

    return get_safe(place)

def back_track(depth):
    # print('d', depth, G)
    global max_safe

    if depth == 3:
        max_safe = max(max_safe, bfs(copy.deepcopy(G)))
        return

    for i in range(N):
        for j in range(M):
            if G[i][j] == 0 :
                G[i][j] = 1
                back_track(depth+1)
                G[i][j] = 0

N, M = map(int, input().split())
G = []
virus = []
visited = [False] * (N * M)

for i in range(N):
    row = list(map(int, input().split()))
    G.append(row)
    for j in range(M):
        if G[i][j] == 2:
            virus.append((i,j))

max_safe = 0
# 벽 3개를 세우는 경우의 수
back_track(depth=0)

print(max_safe)