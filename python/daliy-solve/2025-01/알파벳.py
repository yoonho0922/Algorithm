# https://www.acmicpc.net/problem/1987


dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

def dfs(y, x, depth):
    global answer
    if depth > answer:
        answer = depth

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < R and 0 <= nx < C and G[ny][nx] not in alphas:
            alphas.add(G[ny][nx])
            dfs(ny, nx, depth + 1)
            alphas.remove(G[ny][nx])


R, C = map(int, input().split())
G = [list(input()) for _ in range(R)]

answer = 1
alphas = set(list(G[0][0]))
dfs(0,0, 1)
print(answer)