## input
N = int(input())
S, E = map(int, input().split())
M = int(input())
G = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    line = list(map(int, input().split()))
    G[line[0]][line[1]] = 1
    G[line[1]][line[0]] = 1


distance = [0]*(N+1)
def get_distance(s, e):
    visited = [s]
    queue = [s]
    while queue:
        curr = queue.pop(0)
        for next in range(N+1):
            # curr과 인접하고, 아직 방문하지 않은 노드라면
            if G[curr][next] == 1 and (next not in visited):
                # 종점을 찾았다면
                if next == e:
                    return distance[curr] + 1
                else:
                    distance[next] = distance[curr] + 1
                    visited.append(next)
                    queue.append(next)
    # 친척 관계가 없는 경우
    return -1

## result
print(get_distance(S, E))