N = int(input())

square = [i*i for i in range(1,317)]
d = [0] * 100001

for i in range(1, N+1):
    li = []
    for j in square:
        if i < j:
            break
        li.append(d[i - j])
    d[i] = min(li) + 1

print(d[N])