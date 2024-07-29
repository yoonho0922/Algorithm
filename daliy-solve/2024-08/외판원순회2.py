# https://www.acmicpc.net/problem/10971
def dfs(start, now, value, cnt):
    global ans

    if cnt == N:
        if G[now][start] != 0:
            value += G[now][start]
            ans = min(ans, value)
        return

    if value > ans:
        return

    for i in range(N):
        if not visited[i] and G[now][i] != 0:
            visited[i] = True
            dfs(start, i, value + G[now][i], cnt + 1)
            visited[i] = False


N = int(input())
G = [list(map(int, input().split()))for _ in range(N)]
ans = 1e9
visited = [False] * N

for i in range(N):
    visited[i] = True
    dfs(i, i, 0, 1)
    visited[i] = False

print(ans)