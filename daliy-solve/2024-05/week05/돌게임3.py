# https://www.acmicpc.net/problem/9657

N = int(input())
d = [False] * (N+1)

for i in range(N+1):
    if i <= 4:
        if i in ([1,3,4]):
            d[i] = True
    else:
        d[i] = not (d[i-1] and d[i-3] and d[i-4])

if d[N]:
    print('SK')
else:
    print('CY')
