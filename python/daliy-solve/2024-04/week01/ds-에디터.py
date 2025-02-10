# https://www.acmicpc.net/problem/1406

import sys
readline = sys.stdin.readline

# stack
left = list(map(str, input()))
# reversed stack
right = []

M = int(input())

for _ in range(M):
    cmd = readline().rstrip().split()

    if cmd[0] == 'L':
        if left:
            x = left.pop()
            right.append(x)
    if cmd[0] == 'D':
        if right:
            x = right.pop()
            left.append(x)
    if cmd[0] == 'B':
        if left:
            left.pop()
    if cmd[0] == 'P':
        x = cmd[1]
        left.append(x)

print(''.join(left) + ''.join(right[::-1]))
