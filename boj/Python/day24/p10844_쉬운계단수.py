d = [[0]*10 for _ in range(100)]
d[0] = [1 for _ in range(10)]

for i in range(1, 100):
    for j in range(10):
        if j == 0:
            d[i][j] = d[i - 1][j + 1]
        elif j == 9:
            d[i][j] = d[i - 1][j - 1]
        else:
            d[i][j] = d[i - 1][j - 1] + d[i - 1][j + 1]

N = int(input())
print(sum(d[N-1][1:10]) % 1000000000)
