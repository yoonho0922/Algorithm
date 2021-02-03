import sys
readline = sys.stdin.readline

N = int(readline())
arr = list(map(int, readline().split()))
d = [0] * N
d[0] = arr[0]
for i in range(1, N):
    d[i] = max(d[i-1] + arr[i], arr[i])

print(max(d))