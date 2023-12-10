import sys
readline = sys.stdin.readline

T = int(readline())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, readline().split())
    d = (x1-x2)**2 + (y1-y2)**2

    if [x1, y1, r1] == [x2, y2, r2]:
        print(-1)
    elif (r2-r1)**2 < d < (r1+r2)**2:
        print(2)
    elif (r2-r1)**2 == d or (r1+r2)**2 == d:
        print(1)
    else:
        print(0)