d = [0]*21
d[1] = 1
for i in range(2, 21):
    d[i] = d[i-1] + d[i-2]

N = int(input())
print(d[N])