d = [[0]*15 for _ in range(15)]
for i in range(15):
    d[0][i]=i

for i in range(1, 15):
    for j in range(1, 15):
        for k in range(1, j+1):
            d[i][j] += d[i-1][k]

T = int(input())
for _ in range(T):
    K = int(input())
    N = int(input())
    print(d[K][N])