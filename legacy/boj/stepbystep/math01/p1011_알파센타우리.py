import sys
readline = sys.stdin.readline

T = int(input())
for _ in range(T):
    S, E = map(int, readline().split())
    n = E-S

    i, x, y = 1, 1, 1
    while not n<=x: # i 횟수에 갈 수있는 최대거리 x가 n 이상인걸 찾음
        x = x + y
        i += 1
        if i%2==0:
            y += 1

    print(i)


