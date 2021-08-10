import sys
readline = sys.stdin.readline

while True:
    a, b = map(int, readline().split())
    if [a, b] == [0, 0]:
        break

    if b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')
