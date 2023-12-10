N = int(input())
K = int(input())

ans, l, r = 0, 1, N*N

while l <= r:
    mid = (l + r) // 2
    cnt = 0 # mid 이하인 수의 개수

    for i in range(1, N+1):
        cnt += min(mid//i, N)

    if cnt < K:
        l = mid + 1
    else:
        r = mid - 1
        ans = mid

print(ans)