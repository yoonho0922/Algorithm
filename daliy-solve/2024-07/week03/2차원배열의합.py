# https://www.acmicpc.net/problem/2167


N, M = map(int ,input().split())
G = [list(map(int,input().split())) for _ in range(N)]
S = [[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1, M+1):
        S[i][j] = S[i-1][j] + S[i][j-1] + G[i-1][j-1] - S[i-1][j-1]

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(S[x][y] - S[i-1][y] - S[x][j-1] + S[i-1][j-1])