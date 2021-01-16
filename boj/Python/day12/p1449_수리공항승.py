import sys
readline = sys.stdin.readline

N, L = map(int, readline().split())
arr = list(map(int, readline().split()))
arr.sort()

total = 0
cover = 0

for i in arr:

    if i > cover:
        cover = i + L - 1
        total += 1

print(total)