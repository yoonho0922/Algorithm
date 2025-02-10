# https://www.acmicpc.net/problem/16236

# 1. 먹을 수 있는 게 있는지 확인
# 2. 가장 가까운 먹이 찾기
# 3. 상태 업데이트 (아기상어 위치, 크기, 먹이)

import collections

# 가까운 물고가기 많다면
# (1)가장 위에있는 물고기, 그런 물고기가 많다면
# (2) 가장 왼쪽에 있는 물고기 부터 먹음
dy = [-1,0,0,1]
dx = [0,-1,1,0]


def get_food_location_distance(G, cy, cx, shark_size):
    q = collections.deque()
    visited = [[False]*N for _ in range(N)]

    q.append((cy, cx))
    visited[cy][cx] = True

    distance = -1

    # 가장 가까운 거리에 있는 먹을 수 있는 물고기들
    candis = []

    while q:
        distance += 1
        for _ in range(len(q)):
            y, x = q.popleft()

            # 먹을 수 있는지 검사. 먹이이면서 상어보다 작아야
            if 1<=G[y][x]<=6 and G[y][x] < shark_size:
                # return distance, y, x
                candis.append([distance,y,x])


            # 이동
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0<=ny<N and 0<=nx<N and not visited[ny][nx] and G[ny][nx] <= shark_size:
                    q.append((ny,nx))
                    visited[ny][nx] = True

        if candis:
            food =sorted(candis, key=lambda x: [x[1],x[2]])[0]
            return food[0], food[1], food[2]

    # 먹을 수 있는 게 없음
    return 0, 0, 0

def shark_eat():
    global shark_size, need_eating

    need_eating -= 1

    # 필요한 만큼 먹이를 먹으면 상어 크기 커짐, 다음 필요 먹이 업데이트
    if need_eating == 0:
        shark_size += 1
        need_eating = shark_size


N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]

cy, cx = 0, 0
shark_size = 2
need_eating = 2 # 상어가 크는데 먹어야하는 먹이 수
time = 0

for i in range(N):
    for j in range(N):
        if G[i][j] == 9:
            cy, cx = i, j
            G[i][j] = 0

while True:
    distance, y, x = get_food_location_distance(G, cy, cx, shark_size)


    # 먹을 수 있는게 없음
    if distance == 0:
        break

    # 공간 업데이트
    G[y][x] = 0
    # 상어 위치 업데이트
    cy, cx = y, x
    # 상어 크기, 필요 먹이 업데이트
    shark_eat()
    # 시간 업데이트
    time += distance


print(time)