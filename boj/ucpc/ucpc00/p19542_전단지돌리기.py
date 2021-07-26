from collections import deque
import sys
readline = sys.stdin.readline

def dfs(depth, start):
    global dist

    if depth==D:
        # 전단지를 못 뿌린 곳이 있다면 start를 다음에 방문
        for next in G[start]:
            if not visited[next]:
                q.append(start)
                return
        # 전단지를 다 뿌렸으면 완료.
        return

    for next in G[start]:
        if not visited[next]:
            # print(depth+1, "dfs", next)
            visited[next]=True

            dfs(depth+1, next)


N, S, D = map(int, readline().split())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, readline().split())
    G[a].append(b)
    G[b].append(a)

# for i in range(1,N+1):
#     G[i].sort()

dist = 0
visited = [False]*(N+1)
q = deque()

visited[S]=True
q.append(S)

rvisited=[]

while q:
    cur = q.popleft()
    rvisited.append(cur)
    dfs(0, cur)

visited = [False]*(N+1)

def sub_dfs(start):
    global dist
    if start in rvisited:
        return

    for next in G[start]:
        if not visited[next]:
            visited[next]=True
            dist += 1
            sub_dfs(next)
            dist += 1

dfs(S)
print(dist)

