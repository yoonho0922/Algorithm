import sys
sys.setrecursionlimit(999999999)
readline = sys.stdin.readline
def dfs(x):
    global id
    id += 1
    d[x] = id
    s.append(x)

    parent = d[x]
    for next in G[x]: # next node
        if d[next] == 0: # 방문하지 않은 노드라면 탐색
            parent = min(parent, dfs(next))
        elif not finished[next]: # 방문 했지만 처리 중인 노드라면 사이클
            parent = d[next]

    # 자기 자신이 부모라면 자신이 나올 때 까지 스택에서 꺼냄
    if parent == d[x]:
        scc = []
        while True:
            t = s.pop()
            scc.append(t)
            finished[t] = True
            if t == x:
                break
        scc.sort()
        SCC.append(scc)

    return parent

V, E = map(int, readline().split())
G = [[] for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, readline().split())
    G[a].append(b)

id = 0
d = [0]*(V+1)
finished = [False]*(V+1)
SCC = []
s = []


for i in range(1, V+1):
    if d[i] == 0:
        dfs(i)

SCC.sort()

print(len(SCC))
for scc in SCC:
    print(*scc, -1)