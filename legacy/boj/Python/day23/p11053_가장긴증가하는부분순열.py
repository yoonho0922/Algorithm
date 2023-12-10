import sys
readline = sys.stdin.readline

N = int(readline())
array = list(map(int, readline().split()))

d = [1] * N

for i in range(N):
    for j in range(i):
        if array[j] < array[i]:
            d[i] = max(d[j] + 1, d[i])

print(max(d))