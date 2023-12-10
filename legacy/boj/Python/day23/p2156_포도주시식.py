import sys
readline = sys.stdin.readline

N = int(readline())
array = [0]*10000
for i in range(N):
    array[i] = int(readline())

d = [0]*10000
d[0] = array[0]
d[1] = array[0] + array[1]
d[2] = max(d[1], array[0] + array[2], array[1] + array[2])

for i in range(3, N):
    d[i] = max(d[i-1], array[i] + d[i-2], array[i] + array[i-1] + d[i-3])

print(d[N-1])