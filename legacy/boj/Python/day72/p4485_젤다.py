import heapq
import sys
readline = sys.stdin.readline

INF = 99999999999999999999

def dijkstra(sy, sx, ey, ex):
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    q = []
    dist = [[INF]*N for _ in range(N)]

    dist[sy][sx] = G[sy][sx]
    heapq.heappush(q, (dist[sy][sx], sy, sx))

    while q:
        cur_cost, cy, cx = heapq.heappop(q)

        if dist[cy][cx] < cur_cost:
            continue

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0<=ny<N and 0<=nx<N:
                cost = cur_cost + G[ny][nx]

                if cost < dist[ny][nx]:
                    dist[ny][nx] = cost
                    heapq.heappush(q, (dist[ny][nx], ny, nx))

    return dist[ey][ex]

T=1
while True:
    N = int(readline())
    if N==0:
        break
    G = []
    for _ in range(N):
        row = list(map(int, readline().split()))
        G.append(row)

    print(f"Problem {T}: {dijkstra(0,0, N-1,N-1)}")
    T+=1