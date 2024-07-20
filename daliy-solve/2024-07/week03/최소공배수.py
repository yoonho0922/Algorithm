# https://www.acmicpc.net/problem/13241

def get_gdc(x, y):
    while x % y != 0:
        tmp = x%y
        x = y
        y = tmp
    return y

A, B = map(int, input().split())
gdc = get_gdc(A, B)

print(A*B//gdc)