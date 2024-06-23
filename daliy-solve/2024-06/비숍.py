# https://www.acmicpc.net/problem/1799
# unsolved

def count_up_or_down(up, y, x):
    for i in range(1, N):
        if y+i < N and x+i < N:
            visited[y+i][x+i] += 1 if up else -1
        if y-i >= 0 and x-i >= 0:
            visited[y-i][x-i] += 1 if up else -1
        if y+i < N and x-i >= 0:
            visited[y+i][x-i] += 1 if up else -1
        if y-i >= 0 and x+i < N:
            visited[y-i][x+i] += 1 if up else -1
    visited[y][x] += 1 if up else -1



def dfs(cnt, start):
    global ans
    ans = max(cnt, ans)

    for i in range(start, N*N):
        ny, nx = i//N, i%N
        if visited[ny][nx] == 0 and G[ny][nx] == 1:
            count_up_or_down(True, ny, nx)
            dfs(cnt + 1, i + 1)
            count_up_or_down(False, ny, nx)


N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*N for _ in range(N)]
ans = 0

dfs(0, 0)

print(ans)