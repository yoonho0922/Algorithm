# https://www.acmicpc.net/problem/15989

MAX = 10_000


d = [[0,0,0,0] for _ in range(MAX+1)]
d[1] = [0,1,0,0]
d[2] = [0,1,1,0]
d[3] = [0,1,1,1]

for i in range(4, MAX+1):
    d[i] = [0, 1, sum(d[i-2][:3]), sum(d[i-3])]

T = int(input())
for _ in range(T):
    x = int(input())
    print(sum(d[x]))