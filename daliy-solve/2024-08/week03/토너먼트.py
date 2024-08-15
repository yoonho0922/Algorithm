# https://www.acmicpc.net/problem/1057
def check(n, a, b, step):
    if abs(a-b) == 1 and max(a,b) % 2 == 0:
        return step
    else:
        a = a // 2 if a % 2 == 0 else a // 2 + 1
        b = b // 2 if b % 2 == 0 else b // 2 + 1
        n = n // 2 if n % 2 == 0 else n // 2 + 1

        return check(n, a, b, step + 1)

N, A, B = map(int, input().split())
print(check(N, A, B, 1))
