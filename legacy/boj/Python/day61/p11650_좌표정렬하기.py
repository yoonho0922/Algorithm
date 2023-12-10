import sys
readline = sys.stdin.readline

N = int(readline())
C = []
for _ in range(N):
    C.append(list(map(int, readline().split())))
C.sort()
for i in range(N):
    print(*C[i])