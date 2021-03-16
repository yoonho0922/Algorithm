N = int(input())
d = [0, 1, 2]
for i in range(3, N+1):
    d.append(d[i-2] + d[i-1])
print(d[N]%10007)