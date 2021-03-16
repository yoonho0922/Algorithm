d = [[1, 0], [0, 1]]
for i in range(2, 41):
    a = d[i-1][0] + d[i-2][0]
    b = d[i-1][1] + d[i-2][1]
    d.append([a, b])
T = int(input())
for _ in range(T):
    N = int(input())
    print(d[N][0], d[N][1])