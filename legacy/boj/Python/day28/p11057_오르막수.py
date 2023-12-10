import sys
readline = sys.stdin.readline

N = int(readline())
d = [[1]*10]
d += [[0]*10 for _ in range(N-1)]

for i in range(1, N):
    for j in range(10):
        d[i][j] = sum(d[i-1][j:])

print(sum(d[N-1]) % 10007)