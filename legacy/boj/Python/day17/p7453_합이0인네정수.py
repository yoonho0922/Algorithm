import sys
readline = sys.stdin.readline

N = int(readline())
A, B, C, D = [0]*N, [0]*N, [0]*N, [0]*N
for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, readline().split())

result = 0
case1 = dict()
for i in range(N):
    for j in range(N):
        temp = A[i] + B[j]
        if temp in case1:
            case1[temp] += 1
        else:
            case1[temp] = 1
for i in range(N):
    for j in range(N):
        temp = -(C[i] + D[j])
        if temp in case1:
            result += case1[temp]

print(result)