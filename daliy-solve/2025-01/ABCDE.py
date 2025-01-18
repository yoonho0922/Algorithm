# https://www.acmicpc.net/problem/13023


def dfs(node:int, depth:int):
    if depth == 5:
        global answer
        answer = 1
        return
    for next_node in G[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, depth + 1)
            visited[next_node] = False



N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

answer = 0
visited = [False] * N
for i in range(N):
    visited[i] = True
    dfs(i, 1)
    visited[i] = False
    if answer == 1:
        break
print(answer)

