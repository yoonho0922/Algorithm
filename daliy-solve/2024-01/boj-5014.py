# https://www.acmicpc.net/problem/5014
# 스타트링크

import collections

# 최고층, 현재층, 목표층, up, down
F, S, G, U, D = map(int, input().split())


def bfs():
    q = collections.deque()
    q.append(S)
    visited = [0] * (F + 1)

    while q:
        cur = q.popleft()

        if cur == G:
            print(visited[cur])
            return

        up_floor = cur + U
        down_floor = cur - D

        if up_floor <= F and visited[up_floor] == 0:
            q.append(up_floor)
            visited[up_floor] = visited[cur] + 1
        if down_floor >= 1 and visited[down_floor] == 0:
            q.append(down_floor)
            visited[down_floor] = visited[cur] + 1
    print('use the stairs')


bfs()
