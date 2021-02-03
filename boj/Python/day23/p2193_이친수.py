d = [0]*91
d[0] = 0
d[1] = 1
for i in range(2, 91):
    d[i] = d[i-1] + d[i-2]

N = int(input())
print(d[N]) 