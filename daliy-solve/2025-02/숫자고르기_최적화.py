# http://acmicpc.net/problem/2668

def dfs(cur, start):
    visited[cur] = True
    nxt = G[cur]
    if not visited[nxt]:
        dfs(nxt, start)
    else:
        if nxt == start:
            answer.append(start)


answer = []
N = int(input())
G = [0] * (N + 1)
for i in range(1, N + 1):
    G[i] = int(input())

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    dfs(i, i)

print(len(answer))
print("\n".join(map(str, sorted(answer))))