# https://www.acmicpc.net/problem/16234

from collections import deque

dy = [0,0,1,-1]
dx = [1,-1,0,0]


def check(a, b, L, R):
    return L<=abs(a-b)<=R

def bfs(G, N, visited, cy, cx, L, R):
    q = deque()
    union = [(cy,cx)]
    q.append([cy,cx])
    visited[cy][cx] = True

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0<=ny<N and 0<=nx<N and not visited[ny][nx]:
                if check(G[cy][cx], G[ny][nx], L, R):
                    visited[ny][nx] = True
                    q.append([ny,nx])
                    union.append((ny,nx))

    return union if len(union)!=1 else []

def get_unions(G, N, L, R):
    unions = []
    visited = [[False]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union = bfs(G, N, visited, i, j, L, R)
                # print('i, j, union',i, j, union)
                if union:
                    unions.append(union)

    # print('unions', unions)
    return unions


def distribute(G, union):
    population = sum([G[y][x] for y,x in union]) // len(union)
    # print('union', union)
    # print('population', population)
    for y,x in union:
        G[y][x] = population


N, L, R = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]

ans = 0

while True:
    unions = get_unions(G, N, L, R)

    if not unions:
        break

    ans += 1

    for union in unions:
        distribute(G, union)

    # for i in range(N): print('G', G[i])

print(ans)
