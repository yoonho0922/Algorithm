import sys
readline = sys.stdin.readline

d = [0] * 91
d[1] = 1

for i in range(2, 91):
    d[i] = d[i-1] + d[i-2]

N = int(readline())
print(d[N])