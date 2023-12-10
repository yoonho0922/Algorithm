d = [1, 3]
for i in range(2, 1000):
    d.append(d[i-1] + d[i-2] * 2)

N = int(input())
print(d[N-1] % 10007)