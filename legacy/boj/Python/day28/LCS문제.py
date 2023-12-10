X = input()
Y = input()

N = len(X)
M = len(Y)
c = [[0]*(M + 1) for i in range(N + 1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if X[i-1] == Y[j-1]:
            c[i][j] = c[i-1][j-1] + 1
        else:
            c[i][j] = max(c[i-1][j], c[i][j-1])

print(c[N][M])