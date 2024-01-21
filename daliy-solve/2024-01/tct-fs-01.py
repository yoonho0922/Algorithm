# 음료수 얼려먹기

import sys
import collections
readline = sys.stdin.readline

N, M = map(int, readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input())))
print(graph)

dy = [0,0,1,-1]
dx = [1,-1,0,0]

def bfs(start):
    deque = collections.deque()
    deque.append(start)

    while deque:
        cy, cx = deque.popleft()
        graph[cy][cx] = 1

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<N and 0<=nx<M and graph[ny][nx]==0:
                deque.append((ny, nx))


count = 0
for i in range(N):
    for j in range(M):
        if (graph[i][j]==0):
            bfs(start= (i, j))
            count += 1

print(count)