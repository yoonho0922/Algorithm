# https://www.acmicpc.net/problem/11060

N = int(input())
A = list(map(int,input().split()))
d = [-1] * N
d[0] = 0

for i in range(N):
    if d[i] == -1:
        continue

    for jump in range(1, A[i]+1):
        next = i + jump

        if next < N and d[next] == -1:
            d[next] = d[i]+1

print(d[N-1])