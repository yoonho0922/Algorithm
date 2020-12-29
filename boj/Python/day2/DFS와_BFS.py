## input
N, M, V = map(int, input().split())
G = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    line = list(map(int, input().split()))
    G[line[0]][line[1]] = 1
    G[line[1]][line[0]] = 1

def dfs(s, visited):
    visited.append(s)
    for curr in range(N+1):
        if G[s][curr] == 1 and (curr not in visited):
            dfs(curr, visited)
    return visited

def bfs(s):
    visited = [s]
    queue = [s]
    while queue:
        curr = queue.pop(0)
        for next in range(N+1):
            if G[curr][next] == 1 and (next not in visited):
                visited.append(next)
                queue.append(next)
    return visited

print(*dfs(V,[]))
print(*bfs(V))