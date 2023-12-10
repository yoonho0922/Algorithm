# d[0] = 0
# d[1] = 1 : 1
# d[2] = 2 : 11, 2
# d[3] = 4 : 111, 12, 21, 3
# d[4] = d[3] + d[2] + d[1]

d = [0, 1, 2, 4] + [0] * 9
for i in range(4, 12):
    d[i] = d[i-1] + d[i-2] + d[i-3]

T = int(input())
for _ in range(T):
    N = int(input())
    print(d[N])
