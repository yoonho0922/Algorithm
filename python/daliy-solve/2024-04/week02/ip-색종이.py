# https://www.acmicpc.net/problem/2563

size = 100

N = int(input())
S = [[0]*size for _ in range(size)]

for _ in range(N):
    a, b = map(int, input().split())

    for i in range(a, a+10):
        for j in range(b, b+10):
            S[i][j] = 1

ans = sum([sum(row) for row in S])
print(ans)