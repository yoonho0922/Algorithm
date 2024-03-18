# https://www.acmicpc.net/problem/5430

import sys
readline = sys.stdin.readline


def solve(array, AC):
    reverse_count = 0
    left, right = 0, len(array)-1

    for command in AC:
        if command == 'R':
            reverse_count += 1
        if command == 'D':
            if left > right:
                print('error')
                return

            if reverse_count % 2 == 1:
                right -= 1
            else:
                left += 1

    if left > right:
        print('[]')
    else:
        if reverse_count % 2 == 0:
            result = [array[i] for i in range(left, right+1)]
        else:
            result = [array[i] for i in range(right, left - 1, -1)]

        print('[' + ','.join(map(str, result)) + ']')

T = int(readline())

for _ in range(T):
    AC = readline().rstrip()
    N = int(readline())
    inp = readline()[1:-2]
    array = list(map(int, inp.split(','))) if inp != '' else []

    solve(array, AC)