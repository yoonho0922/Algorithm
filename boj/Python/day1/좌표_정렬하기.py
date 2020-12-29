import sys

N = int(sys.stdin.readline())
so = []
for i in range(N):
    so.append(list(map(int,sys.stdin.readline().split())))
so.sort(key=lambda x: (x[0], x[1]))
for i in so:
    print(i[0], i[1])