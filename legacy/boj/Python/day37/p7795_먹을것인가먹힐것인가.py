import sys
readline = sys.stdin.readline

T = int(readline())
for _ in range(T):
    N, M = map(int, readline().split())
    A = list(map(int, readline().split()))
    B = list(map(int, readline().split()))

    A.sort()
    B.sort()
    j, ans = 0, 0

    for i in range(N):
        while j < M:
            if B[j] < A[i]:
                j += 1
            else:
                break
        ans += j
    print(ans)