import heapq
import sys
readline = sys.stdin.readline

INF=999999
type={'Subway':0, 'Bus':1, 'Taxi':2,
      'Airplane':3, 'KTX':4, 'S-Train':5,
      'V-Train':6, 'ITX-Saemaeul':7,
      'ITX-Cheongchun':8, 'Mugunghwa':9}
# 5,6->50%, 7,8,9->free

def dijkstra_nae(s, e):
    dist = [INF]*N
    q = []

    dist[s] = 0
    heapq.heappush(q, (dist[s], s))

    while q:
        cur_dist, cur_node = heapq.heappop(q)

        if dist[cur_node] < cur_dist:
            continue
        for d, v, t in G[cur_node]:
            if 7<=t<=9: # free
                cost = cur_dist
            elif 5<=t<=6: # 50%
                cost = cur_dist + d/2
            else:
                cost = cur_dist + d

            if cost < dist[v]:
                dist[v] = cost
                heapq.heappush(q, (dist[v], v))

    return dist[e]

def dijkstra(s, e):
    dist = [INF]*N
    q = []

    dist[s] = 0
    heapq.heappush(q, (dist[s], s))

    while q:
        cur_dist, cur_node = heapq.heappop(q)

        if dist[cur_node] < cur_dist:
            continue
        for d, v, type in G[cur_node]:
            cost = cur_dist + d
            if cost < dist[v]:
                dist[v] = cost
                heapq.heappush(q, (dist[v], v))

    return dist[e]


N, R = map(int, readline().split())
row = list(readline().split())
city = {}
for i in range(N):
    if city.get(row[i]):
        continue
    city[row[i]] = i

M = int(readline())
plan = list(readline().split())

K = int(readline())
G = [[] for _ in range(N)]
for _ in range(K):
    # KTX Seoul Busan 20000
    vehicle, start, end, cost = readline().split()
    G[city[start]].append((int(cost), city[end], type[vehicle]))
    G[city[end]].append((int(cost), city[start], type[vehicle]))

default_cost = 0
nae_cost = R
for i in range(M-1):
    # print(plan[i], plan[i+1], dijkstra(city[plan[i]], city[plan[i+1]]))
    # print(plan[i], plan[i+1], dijkstra_nae(city[plan[i]], city[plan[i+1]]))
    default_cost += dijkstra(city[plan[i]], city[plan[i+1]])
    nae_cost += dijkstra_nae(city[plan[i]], city[plan[i+1]])

# print(nae_cost, default_cost)
print('Yes' if nae_cost < default_cost else 'No')

# for i in range(N):
#     for c, s, e in G[i]:
#         print(i, s, e, c)