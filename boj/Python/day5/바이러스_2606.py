def bfs(s):
    total = 0
    q = [s] # queue
    v = [s] # visited
    while q:
        curr = q.pop(0)
        # 모든 노드를 검사
        for next in range(N+1):
            # 연결되어 있고 방문하지 않았다면
            if G[curr][next] and next not in v:
                q.append(next)
                v.append(next)
                total += 1
    return total
# 입력
N = int(input())
M = int(input())
G = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    line = list(map(int, input().split()))
    G[line[0]][line[1]] = 1
    G[line[1]][line[0]] = 1

print(bfs(1))