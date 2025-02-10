# https://www.acmicpc.net/problem/2477

K = int(input())
lines = [list(map(int, input().split())) for _ in range(6)]
lines += lines

X, Y = 0, 0 # 큰 변
a, b = 0, 0 # 작은 변
for i in range(1, len(lines) - 4):
    if lines[i][0] == lines[i+2][0] and lines[i+1][0] == lines[i+3][0]:
        a, b = lines[i+1][1], lines[i+2][1]
        X, Y = lines[i-1][1], lines[i+4][1]

area = X * Y - a * b
# print(X, Y, a, b)
# print(area)
print(area * K)
