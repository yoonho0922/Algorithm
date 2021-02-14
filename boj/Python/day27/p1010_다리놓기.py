import sys
readline = sys.stdin.readline

T = int(readline())
for _ in range(T):
    N, M = map(int, readline().split())
    ans = 1
    for i in range(M-N+1, M+1):
        ans *= i
    for i in range(1, N+1):
        ans //= i
    print(ans)