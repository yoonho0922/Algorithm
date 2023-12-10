import sys
readline = sys.stdin.readline

def converse(row, col):

    for i in range(row, row+3):
        for j in range(col, col + 3):

            if A[i][j] == 1:
                A[i][j] = 0
            else:
                A[i][j] = 1

def solve():

    cnt = 0

    for i in range(N-2):
        for j in range(M-2):

            if A[i][j] != B[i][j]:
                converse(i, j)
                cnt += 1

    return cnt


N, M = map(int, readline().split())

A = [[0]*M for _ in range(N)]
B = [[0]*M for _ in range(N)]

for i in range(N):
    l = readline()
    for j in range(M):
        A[i][j] = int(l[j])

for i in range(N):
    l = readline()
    for j in range(M):
        B[i][j] = int(l[j])

cnt = solve()

for i in range(N):
    if A[i] != B[i]:
        cnt = -1
        break

print(cnt)