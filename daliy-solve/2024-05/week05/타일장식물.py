# https://www.acmicpc.net/problem/13301

N = int(input())
d = [0, 1]

for i in range(2, N+1):
    d.append(d[i-1] + d[i-2])

print((d[N]*2 + d[N-1]) * 2)