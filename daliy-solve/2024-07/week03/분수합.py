# https://www.acmicpc.net/problem/1735


def get_gdc(x, y):
    while x % y != 0:
        mod = x % y
        x = y
        y = mod

    return y


a, b = map(int, input().split())
c, d = map(int, input().split())

num = a*d + b*c
denom = b*d

gdc = get_gdc(num, denom)

print(num//gdc, denom//gdc)