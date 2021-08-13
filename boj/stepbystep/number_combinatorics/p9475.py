T = int(input())
for _ in range(T):
    N = int(input())
    d = {}
    for _ in range(N):
        a, b = input().split()
        if d.get(b):
            d[b] += 1
        else:
            d[b] = 1

    ans = 1
    for i in d.values():
        ans *= i+1
    print(ans-1)