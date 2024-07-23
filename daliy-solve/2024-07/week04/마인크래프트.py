# https://www.acmicpc.net/problem/18111

MAX_HEIGHT = 256
MIN_HEIGHT = 0


def leveling(height):
    blocks = B
    time = 0

    for i in range(N):
        for j in range(M):
            # 1. 블록을 제거한다
            if G[i][j] > height:
                gap = G[i][j] - height
                blocks += gap
                time += gap * 2
            # 2. 블록을 채운다
            elif G[i][j] < height:
                gap = height - G[i][j]
                blocks -= gap
                time += gap * 1

    # 소요 시간, 남은 블록
    return time, blocks

N, M, B = map(int ,input().split())
G = [list(map(int, input().split())) for _ in range(N)]

l, r, least_time, highest_land = MIN_HEIGHT, MAX_HEIGHT, 1e9, 0,

for height in range(MAX_HEIGHT+1):
    time, blocks = leveling(height)
    # 남은 블록이 0 이상 이면 만들 수 있는 높이다
    if blocks >= 0:
        # 최소 시간으로 만들 수 있는 높이를 구한다
        if time <= least_time:
            least_time = time
            # 최소 시간이 같다면 만들 수 있는 가장 높은 높이를 구한다
            highest_land = max(highest_land, height)

print(least_time, highest_land)