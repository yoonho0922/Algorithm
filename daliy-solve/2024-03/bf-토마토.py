# https://www.acmicpc.net/problem/7576

import sys
import collections
readline = sys.stdin.readline

# 동, 남, 서, 북
dy = [0,1,0,-1]
dx = [1,0,-1,0]


def is_all_ripe(G):
    for row in G:
        if 0 in row:
            return False
    return True

def get_day_count(G, N, M, init_ripes):
    day = -1
    q = collections.deque()

    for y, x in init_ripes:
        q.append((y, x))

    while q:
        for _ in range(len(q)):
            # 익은 토마토 좌표
            cy, cx = q.popleft()

            for i in range(4):
                ny = cy + dy[i]
                nx = cx + dx[i]

                if 0<=ny<N and 0<=nx<M and G[ny][nx]==0:
                    G[ny][nx] = 1
                    q.append((ny,nx))

        day += 1

    if is_all_ripe(G):
        return day
    else:
        return -1

M, N = map(int, input().split())
G = []
ripes = []

for i in range(N):
    row = list(map(int, readline().split()))
    G.append(row)
    for j in range(M):
        if row[j] == 1:
            ripes.append((i, j))

print(get_day_count(G, N, M, ripes))