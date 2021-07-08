import sys
readline = sys.stdin.readline

N = int(readline())
lines = []
for _ in range(N):
    lines.append(list(map(int, readline().split())))

lines.sort()

d = [1]*N

for i in range(N):
    for j in range(i):
        if lines[j][1] < lines[i][1]:
            d[i] = max(d[i], d[j]+1)

print(N-max(d))