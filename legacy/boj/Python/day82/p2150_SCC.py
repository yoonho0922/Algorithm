import sys
readline = sys.stdin.readline

def dfs(x):
    visited[x] = True
    s.append(x)
    parent = x

    for next in G[x]: # next node
        if not visited[next]: # 방문하지 않은 노드라면 탐색
            parent = min(parent, dfs(next))
        elif not finished[next]: # 방문 했지만 처리 중인 노드라면 사이클
            parent = min(parent, next)

    # 자기 자신이 부모라면 자신이 나올 때 까지 스택에서 꺼냄
    if parent == x:
        print(x)
        scc = []
        while True:
            t = s.pop()
            scc.append(t)
            finished[t] = True
            if t == x:
                break
        scc.sort()
        SCC.append(scc)

    # print(x, parent)

    return parent

V, E = map(int, readline().split())
G = [[] for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, readline().split())
    G[a].append(b)

visited = [False]*(V+1)
finished = [False]*(V+1)
SCC = []
s = []


for i in range(1, V+1):
    if not visited[i]:
        dfs(i)

print(len(SCC))
for scc in SCC:
    print(scc)