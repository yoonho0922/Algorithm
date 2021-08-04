N, S, M = map(int, input().split())
V = list(map(int, input().split()))

d = [[False]*(M+1) for _ in range(N)]

for x in [S-V[0], S+V[0]]:
    if 0<=x<=M:
        d[0][x]=True

for i in range(1, N):

    for j in range(M+1):
        if d[i-1][j]:
            for x in [j-V[i], j+V[i]]:
                if 0<=x<=M:
                    d[i][x]=True
ans=-1
for i in range(M+1):
    if d[N-1][i]:
        ans = max(ans, i)

print(ans)