import sys
readline = sys.stdin.readline

T = int(readline())

for _ in range(T):
    N = int(readline())
    A = [0] + list(map(int, readline().split()))
    B = [0] + list(map(int, readline().split()))
    da, db = [0]*(N+1), [0]*(N+1)

    for i in range(1, N+1):
        da[i] = max(db[i-1] + A[i], da[i-1])
        db[i] = max(da[i-1] + B[i], db[i-1])
    print(max(da[N], db[N]))