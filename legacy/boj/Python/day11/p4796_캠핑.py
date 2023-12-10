import sys
readline = sys.stdin.readline

i = 1

while True:
    L, P, V = map(int, readline().split())
    if L+P+V == 0:
        break

    total_day = (V // P) * L
    remainder = V % P

    total_day += min(V % P, L)

    print('Case %d: %d' %(i, total_day))
    i += 1
