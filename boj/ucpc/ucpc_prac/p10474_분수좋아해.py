import sys
readline = sys.stdin.readline

while True:
    x, y = map(int, readline().split())
    if x==0 and y==0:
        break

    print(x//y, f"{x%y} / {y}")