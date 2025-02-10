# https://www.acmicpc.net/problem/1189


dy = [0, 0, 1, -1]
dx = [1, -1 ,0 , 0]

def dfs(y, x, depth):
    if depth == K - 1:
        if [y, x] == [0, C - 1]:
            # 집에 도착
            global answer
            answer += 1
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<R and 0<=nx<C and G[ny][nx] == '.':
            G[ny][nx] = '!'
            dfs(ny, nx, depth + 1)
            G[ny][nx] = '.'


R, C, K = map(int, input().split())
G = [list(input()) for _ in range(R)]

answer = 0
G[R - 1][0] = '!'
dfs(R - 1, 0, 0)
print(answer)
