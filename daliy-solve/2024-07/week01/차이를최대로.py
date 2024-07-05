# https://www.acmicpc.net/problem/10819

def dfs(mixed):
    if len(mixed) == N:
        total_abs = 0
        for i in range(1, N):
            total_abs += abs(mixed[i-1] - mixed[i])
        global ans
        ans = max(ans, total_abs)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(mixed + [A[i]])
            visited[i] = False

N = int(input())
A = list(map(int, input().split()))

ans = 0
visited = [False]*N
dfs([])

print(ans)