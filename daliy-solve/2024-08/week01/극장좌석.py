# https://www.acmicpc.net/problem/2302

N = int(input())
M = int(input())
vips = [0]

for _ in range(M):
    vips.append(int(input()))

d = [1] * (N+1)

for i in range(2, N+1):
    d[i] = d[i-1] + d[i-2]

total = 1
vips.sort()

for i in range(1, M+1):
    gap = vips[i] - vips[i-1] - 1
    total *= d[gap]

# 끝 구간 곱하기
last_gap = N - vips[-1]
total *= d[last_gap]

print(total)