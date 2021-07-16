from collections import deque
import sys
readline = sys.stdin.readline

def bfs():
    q=deque()
    visited = [0]*(N+1)
    cnt, depth = 0, 0

    q.append(1)
    visited[1]=1

    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            child = 0
            for next in G[cur]:
                if not visited[next]:
                    q.append(next)
                    visited[next]=1
                    child+=1
            if child==0:
                cnt += depth
        depth +=1
    return cnt


# input
N = int(readline())
G = {i:[] for i in range(1,N+1)}
for _ in range(N-1):
    a, b = map(int, readline().split())
    G[a].append(b)
    G[b].append(a)

cnt = bfs()
print("Yes" if cnt%2==1 else "No")