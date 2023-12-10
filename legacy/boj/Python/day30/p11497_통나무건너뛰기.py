import sys
readline = sys.stdin.readline

T = int(readline())
for _ in range(T):
    N = int(readline())
    L = list(map(int, readline().split()))

    L.sort()
    heights = []

    for i in range(N - 2):
        heights.append(L[i+2] - L[i])

    print(max(heights))