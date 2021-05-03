import sys
readline = sys.stdin.readline

N = int(readline())
M = []
for _ in range(N):
    age, name = list(readline().split())
    M.append([int(age), name])

M.sort(key=lambda x: x[0])

for i in range(N):
    print(*M[i])