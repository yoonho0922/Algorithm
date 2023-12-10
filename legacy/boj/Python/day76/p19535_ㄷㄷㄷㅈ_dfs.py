import sys
sys.setrecursionlimit(99999999)
readline = sys.stdin.readline


def dfs(node, depth):
    global du, ga

    # get ga
    if len(G[node]) >=3:
        m = len(G[node])
        ga += m*(m-1)*(m-2)//6

    for next in G[node]:
        if not visited[next]:
            visited[node]=True
            dfs(next, depth+1)
            # get du
            if len(G[node]) >= 2 and len(G[next]) >= 2:
                du += (len(G[node]) - 1) * (len(G[next]) - 1)


N = int(readline())
G = [[]*(N+1) for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, readline().split())
    G[a].append(b)
    G[b].append(a)

du, ga, = 0, 0
visited = [False]*(N+1)

visited[1] = True
dfs(1, 0)

if du == ga*3:
    print("DUDUDUNGA")
elif du > ga*3:
    print("D")
elif ga < ga*3:
    print("G")