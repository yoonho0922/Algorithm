import sys
import math
readline = sys.stdin.readline

T = int(readline())
for _ in range(T):
    P, Q, A, B, C, D = map(int,readline().split())
    # 1. 베리 -> 코인
    bit, coin = P, Q//C*D

    X = abs(bit-coin)//(A+B)
    ans = 0

    for x in [X-1, X, X+1]:
        ans = max(ans, min(bit - A*x, coin + B*x))
        ans = max(ans, min(bit + A*x, coin - B*x))

    print(ans if ans>0 else 0)