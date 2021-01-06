import sys
readl = sys.stdin.readline

N = int(readl())
arr = []
for i in range(N):
    arr.append(int(readl()))

arr.sort()

for i in range(N):
    print(arr[i])