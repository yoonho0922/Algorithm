# https://www.acmicpc.net/problem/10974


def dfs(permutation):
    if len(permutation) == N:
        print(*permutation)
        return

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            dfs(permutation + [i])
            visited[i] = False

N = int(input())

visited = [False] * (N+1)
dfs([])