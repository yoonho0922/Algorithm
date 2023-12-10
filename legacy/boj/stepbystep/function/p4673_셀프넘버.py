def d(n):
    res = n
    for num in str(n):
        res += int(num)
    return res

def sol(n):
    if n>10000 or not self_number[n]:
        return
    self_number[n] = False
    sol(d(n))


self_number=[True]*10001
for i in range(1,10001):
    sol(d(i))

for i in range(1, 10001):
    print("{}\n".format(i) if self_number[i] else '',end='')