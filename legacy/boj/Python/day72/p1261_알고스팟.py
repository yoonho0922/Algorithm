import heapq

INF=9999999999

def dijkstra(sy, sx, ey, ex):
    dy=[1,-1,0,0,]
    dx=[0,0,1,-1]
    q=[]
    dist=[[INF]*M for _ in range(N)]

    dist[sy][sx]=0
    heapq.heappush(q, (dist[sy][sx], sy, sx))

    while q:
        cur_dist, cy, cx = heapq.heappop(q)

        if dist[cy][cx] < cur_dist:
            continue

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0<=ny<N and 0<=nx<M:
                cost = cur_dist + G[ny][nx]

                if cost < dist[ny][nx]:
                    dist[ny][nx] = cost
                    heapq.heappush(q, (dist[ny][nx], ny, nx))

    return dist[ey][ex]

M, N = map(int, input().split())
G = [list(map(int, input())) for _ in range(N)]

print(dijkstra(0,0,N-1,M-1))