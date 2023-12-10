N = int(input())
p = []
for _ in range(N):
    p.append(list(map(int, input().split())))
d = [[p[0][0]]]
for i in range(1, N):
    layer = []
    for j in range(i+1):
        if j==0:
            layer.append(d[i-1][0] + p[i][j])
        elif j==i:
            layer.append(d[i - 1][j-1] + p[i][j])
        else:
            layer.append(max(d[i-1][j-1], d[i-1][j]) + p[i][j])
    d.append(layer)
print(max(d[N-1]))