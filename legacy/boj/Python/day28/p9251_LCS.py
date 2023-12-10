import sys
readline = sys.stdin.readline

S1 = readline().strip()
S2 = readline().strip()

N1 = len(S1)
N2 = len(S2)
d = [[0]*(N2 + 1) for i in range(N1 + 1)]

for i in range(1, N1+1):
    for j in range(1, N2+1):
        if S1[i-1] == S2[j-1]:
            d[i][j] = d[i-1][j-1] + 1
        else:
            d[i][j] = max(d[i-1][j], d[i][j-1])

print(d[N1][N2])