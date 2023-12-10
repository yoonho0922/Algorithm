N = int(input())
p = []
for _ in range(N):
    p.append(list(map(int, input().split())))

d = [[0]*3 for _ in range(N+1)]
for i in range(1, N+1):
    d[i][0] = p[i-1][0] + min(d[i-1][1], d[i-1][2])
    d[i][1] = p[i-1][1] + min(d[i-1][0], d[i-1][2])
    d[i][2] = p[i-1][2] + min(d[i-1][0], d[i-1][1])

print(min(d[N]))