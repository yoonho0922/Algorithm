# https://www.acmicpc.net/contest/official/list

dy = [0,0,1,-1]
dx = [1,-1,0,0]

def dfs(cy, cx):
    if [cy,cx] == [N-1, M-1]:
        return 1

    count = 0

    for i in range(4):
        ny = cy + dy[i]
        nx = cx + dx[i]
        if 0<=ny<N and 0<=nx<M and G[cy][cx]>G[ny][nx]:
            if dp[ny][nx] == -1:
                count += dfs(ny, nx)
            else:
                count += dp[ny][nx]

    dp[cy][cx] = count
    return count



N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1]*M for _ in range(N)] # [y,x]부터 목적지까지 도달할 수 있는 경우의 수
dp[N-1][M-1] = 1

dfs(0,0)

print(dp[0][0])