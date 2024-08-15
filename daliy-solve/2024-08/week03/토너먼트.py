# https://www.acmicpc.net/problem/1057

N, A, B = map(int, input().split())
a, b = A-1, B-1
step = 0
while a != b:
    step += 1
    a //= 2
    b //= 2
print(step)