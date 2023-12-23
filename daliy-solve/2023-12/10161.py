# https://www.acmicpc.net/problem/10162
# 전자레인지

import sys
readline = sys.stdin.readline

T = int(readline())

a, b, c = 5*60, 1*60, 10

count_a, count_b, count_c = 0, 0, 0


def solve():
    total = T

    count_a = total//a
    total %= a

    count_b = total//b
    total %= b

    count_c = total//c
    total %= c

    if (total==0):
        print(count_a, count_b, count_c)
    else:
        print(-1)

solve()

