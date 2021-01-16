import sys
readline = sys.stdin.readline

N = int(readline())
s = []
for _ in range(N):
    s.append(int(readline()))

total = 0

for i in range(N-1, 0, -1):

    while s[i-1] >= s[i]:
        s[i-1] -= 1
        total += 1

print(total)