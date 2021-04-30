N = int(input())
p = [0] * 301
d = [0] * 301
for i in range(N):
    p[i] = int(input())

d[1] = p[0]
d[2] = p[0] + p[1]

for i in range(3, N + 1):
    d[i] = p[i - 1] + max(d[i - 2], p[i - 2] + d[i - 3])

print(d[N])