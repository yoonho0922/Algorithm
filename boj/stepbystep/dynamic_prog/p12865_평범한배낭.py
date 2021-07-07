import sys
readline = sys.stdin.readline

N, K = map(int, readline().split())
p = [[0]]
for _ in range(N):
    p.append(list(map(int, readline().split())))

d = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        w, v = p[i][0], p[i][1]
        if j < w:
            d[i][j] = d[i - 1][j]
        else:
            d[i][j] = max(d[i - 1][j], v + d[i-1][j-w])

ans = 0
for i in range(N+1):
    ans = max(ans, d[i][K])
print(ans)