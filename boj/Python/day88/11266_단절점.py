import sys
sys.setrecursionlimit(9999999)
readline = sys.stdin.readline

def dfs(u, v, isRoot): # v는 u의 부모
    global num, cnt
    num += 1
    dfn[u] = low[u] = num

    sub = 0 # dfs 트리에서 자식 수

    for w in G[u]:
        sub += 1

        if dfn[w] < 0: # 하위 노드라면 (방문하지 않았다면)
            dfs(w, u, False)
            low[u] = min(low[u], low[w])

            # 분절점 체크
            if isRoot: continue

            if not ap[u] and low[w] >= dfn[u]:
                cnt += 1
                ap[u] = True
        elif w != v: # 부모가 아닌 상위 노드라면
            low[u] = min(low[u], low[w])

    if isRoot and sub>1:
        cnt += 1
        ap[u] = True





V, E = map(int, readline().split())
G = [[]*(V+1) for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, readline().split())
    G[a].append(b)
    G[b].append(a)

dfn = [-1]*(V+1)
low = [-1]*(V+1)
num = 0

ap = [False]*(V+1)
cnt = 0

for i in range(1, V+1):
    if dfn[i] < 0:
        dfs(i, -1, True)


print(cnt)
for i in range(1, V+1):
    if ap[i]:
        print(i, end=' ')