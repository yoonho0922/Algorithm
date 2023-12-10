import sys
readline = sys.stdin.readline

T = int(readline())
for _ in range(T):
    N = int(readline())
    init = readline().strip()
    target = readline().strip()

    W, B = 0, 0
    i = 0
    while i < N:
        if init[i] == target[i]:
            i += 1
        else:
            if init[i] == 'B':
                B += 1
            else:
                W += 1
            i += 1

    count = min(B, W) + abs(B-W)
    print(count)
