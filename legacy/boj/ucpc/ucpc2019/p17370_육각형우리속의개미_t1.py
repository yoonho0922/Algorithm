def sol(depth, prev, cy, cx):
    global cnt

    if depth >= N:
        return

    # 개미가 두 갈래 방향 탐색
    for i in next_idx[prev]: # i = 5, 1
        ny = cy + dy[i]
        nx = cx + dx[i]
        # 가려는 길이 이미 방문한 곳이라면
        if visited[ny][nx]:
            # 다음 방문이 N 번째 방향 전환이라면
            if depth+1 == N:
                cnt += 1
            continue

        visited[ny][nx] = 1
        sol(depth+1, i, ny, nx)
        visited[ny][nx] = 0

N = int(input())
visited = [[0]*100 for _ in range(100)]
cnt = 0

dy = [2,1,-1,-2,-1,1]
dx = [0,1,1,0,-1,-1]
next_idx = [[5,1], [0,2], [1,3], [2,4], [3,5], [0,4]]

visited[50][50] = 1
visited[52][50] = 1

sol(0, 0, 52, 50)
print(cnt)