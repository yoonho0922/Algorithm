import sys
readline = sys.stdin.readline

N = int(readline())
s = [0]*10001
for _ in range(N):
    i = int(readline())
    s[i] += 1
for i in range(1, 10001):
    for j in range(s[i]):
        print(i)