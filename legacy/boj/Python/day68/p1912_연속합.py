N = int(input())
p = list(map(int, input().split()))
d = [p[0]]

for i in range(1, N):
    d.append(max(d[i-1] + p[i], p[i]))

print(max(d))