N = int(input())
A = list(map(int, input().split()))

s = []
NGE = [-1]*N

for i in range(N-1, -1, -1):
    while len(s)>0 and A[i] >= s[-1]:
        s.pop()

    if len(s) == 0:
        s.append(A[i])
        continue

    NGE[i] = s[-1]
    s.append(A[i])

print(' '.join(list(map(str, NGE))))