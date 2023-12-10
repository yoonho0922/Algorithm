import sys
readline = sys.stdin.readline

def dfs(cur):

    for next in range(N):
        if matrix[cur][next] == 1 and not visited[next]:
            visited[next] = 1
            dfs(next)

N = int(readline())
matrix = []

for _ in range(N):
    m = list(map(int, readline().split()))
    matrix.append(m)

ans = [[0]*N for _ in range(N)]

for i in range(N):
    visited = [0] * N
    dfs(i)
    print(*visited)