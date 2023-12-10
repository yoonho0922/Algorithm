import sys
readline = sys.stdin.readline

N = int(readline())
P = list(map(int, readline().split()))
d = [0] * 10001
d[0] = P[0]

for i in range(1, N):
    li = []
    for j in range(i//2, -1, -1):
        li.append(d[i-1-j] + d[j])
    li.append(P[i])
    d[i] = max(li)

print(d[N-1])