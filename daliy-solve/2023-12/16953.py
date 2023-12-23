# https://www.acmicpc.net/status?user_id=yoonho0922&problem_id=16953&from_mine=1
# A -> B

import sys
readline = sys.stdin.readline

A, B = map(int, readline().split())

def solve(num):
    if num == B:
        return 1
    if num > B:
        return float('inf')

    result1 = solve(num * 2)
    result2 = solve(int(str(num) + '1'))

    return 1 + min(result1, result2)

result = solve(A)
print(result if result != float('inf') else -1)