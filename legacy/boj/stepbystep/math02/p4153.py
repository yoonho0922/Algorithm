import sys
readline = sys.stdin.readline

while True:
    p = list(map(int, readline().split()))
    if p == [0,0,0]:
        break

    p.sort()

    if p[2]**2 == p[0]**2 + p[1]**2:
        print("right")
    else:
        print("wrong")