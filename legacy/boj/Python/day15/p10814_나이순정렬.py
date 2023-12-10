import sys
readline = sys.stdin.readline

N = int(readline())
members = []
for _ in range(N):
    L = readline().strip().split()
    members.append((int(L[0]), L[1]))

members.sort(key=lambda x: x[0])

for m in members:
    print(m[0], m[1])