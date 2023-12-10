import sys
readline = sys.stdin.readline

N = int(readline())
array = [0] * (301)
for i in range(1, N + 1):
    array[i] = int(readline())

d = [0] * (301)
d[1] = array[1]
d[2] = array[2] + array[1]

for i in range(3, N+1):
    d[i] = max(d[i-2], d[i-3] + array[i-1]) + array[i]

print(d[N])
