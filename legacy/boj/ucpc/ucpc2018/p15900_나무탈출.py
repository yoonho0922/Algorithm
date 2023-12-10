'''
recursion error : 깊이가 500,000이 될 수 도 있음 -> BOJ 채점 서버는 최대 1000 까지만
'''
import sys
readline = sys.stdin.readline

def dfs(depth, cur):
    global cnt
    isLeaf=True

    for next in G[cur]:
        if not visited[next]:
            visited[next]=1
            dfs(depth+1, next)
            isRoot=False

    if isLeaf:
        cnt += depth

# input
N = int(readline())
G = {i:[] for i in range(1,N+1)}
for _ in range(N-1):
    a, b = map(int, readline().split())
    G[a].append(b)
    G[b].append(a)

cnt = 0
visited = [0]*(N+1)
visited[1]=1
dfs(0, 1)

print("YES" if cnt%2==1 else "NO")