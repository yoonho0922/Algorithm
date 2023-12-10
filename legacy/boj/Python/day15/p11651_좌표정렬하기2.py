import sys
readline = sys.stdin.readline

N = int(readline())
coordinates = []
for _ in range(N):
    L = list(map(int, readline().split()))
    coordinates.append((L[0], L[1]))

coordinates.sort(key=lambda x: (x[1], x[0]))

for c in coordinates:
    print(c[0], c[1])