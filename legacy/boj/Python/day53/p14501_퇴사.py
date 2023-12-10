import sys
readline = sys.stdin.readline

N = int(readline())
T, P = [], []
for _ in range(N):
    t, p = map(int, readline().split())
    T.append(t)
    P.append(p)

d = [0] * (N+1)

for i in range(N-1, -1, -1):
    if T[i] > N-i:
        d[i] = d[i+1]
        continue
    d[i] = max(P[i] + d[i + T[i]], d[i+1])

print(d[0])
