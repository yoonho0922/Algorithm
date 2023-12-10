# 북 동 남 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def rotate(cy, cx, cd):
    for i in range(1, 5):
        # 왼쪽 방향 회전
        nd = cd-i if cd-i >= 0 else cd + 4 - i # 0-1 -> 3, 0-2 -> 2, 1-3 -> 2, 2-3 ->3
        ny = cy + dy[nd]
        nx = cx + dx[nd]

        # 2. 왼쪽 방향을 청소해야 되면 1번으로
        if (0<=ny<N and 0<=nx<M) and G[ny][nx] == 0 and not visited[ny][nx]:
            # print("청소해야됨 : ", ny, nx, nd)
            return ny, nx, nd

    return cy, cx, cd

def sol(cy, cx, cd):
    cnt = 0

    while True:
        # print(cy, cx, cd)
        # 1. 현재 위치를 청소한다
        if not visited[cy][cx]:
            # print(cnt+1, cy, cx, cd)
            cnt += 1
            visited[cy][cx] = True

        ny, nx, cd = rotate(cy, cx, cd)

        # 2. 왼쪽 방향을 청소해야 되면 1 번으로
        if [ny, nx] != [cy, cx]:
            cy, cx = ny, nx
            continue

        # 3. 청소할 방향 없는 경우 후진하고 2번으로
        # 방향을 유지한채로 후진
        # nd = cd-2 if cd-2 >= 0 else 2+cd # 1-2 -> 3, 0-2 -> 2
        cy = cy - dy[cd]
        cx = cx - dx[cd]
        # print("후진")

        # 4. 후진이 불가능할 경우 멈춤
        if not (0<=cy<N and 0<=cx<M) or G[cy][cx] == 1:
            break

    return cnt

N, M = map(int, input().split())
r, c, d = map(int, input().split())
G = []
for _ in range(N):
    G.append(list(map(int, input().split())))

visited = [[False]*M for _ in range(N)]

print(sol(r, c, d))