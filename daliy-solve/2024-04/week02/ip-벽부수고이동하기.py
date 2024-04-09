# https://www.acmicpc.net/problem/2206

from collections import deque
import sys
readline = sys.stdin.readline

INF = 1e9

dy = [0,0,1,-1]
dx = [1,-1,0,0]

def get_shortest(graph, N, M):
    q = deque()
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

    # y, x, 0: not broken 1: broken
    q.append([0,0,0])
    visited[0][0][0] = 1

    while q:
        cy, cx, broken = q.popleft()

        if [cy, cx] == [N-1, M-1]:
            return visited[cy][cx][broken]

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if not(0<=ny<N and 0<=nx<M):
                continue

            # 벽이 아니면서 방문하지 않은 경우 다음 칸 이동
            if graph[ny][nx] == 0 and visited[ny][nx][broken] == 0:
                q.append([ny,nx,broken])
                visited[ny][nx][broken] = visited[cy][cx][broken] + 1

            # 벽일 경우 벽을 부순 적이 없다면 벽을 부수고 다음 칸 이동
            if graph[ny][nx] == 1 and broken == 0:
                q.append([ny,nx,1])
                visited[ny][nx][1] = visited[cy][cx][0] + 1

    return -1


N, M = map(int, input().split())
G = [list(map(int, readline().rstrip())) for _ in range(N)]

ans = get_shortest(G, N, M)
print(ans)