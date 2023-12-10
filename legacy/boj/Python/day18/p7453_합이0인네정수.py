import sys
readline = sys.stdin.readline

N = int(readline())
A, B, C, D = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab = dict()
result = 0

for i in range(N):
    for j in range(N):
        sum_ab = A[i] + B[j]
        if ab.get(sum_ab):
            ab[sum_ab] += 1
        else:
            ab[sum_ab] = 1

for i in range(N):
    for j in range(N):
        sum_cd = (C[i] + D[j])
        if ab.get(-sum_cd):
            result += ab[-sum_cd]

print(result)
