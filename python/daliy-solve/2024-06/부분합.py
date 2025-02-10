# https://www.acmicpc.net/problem/1806

INF = 1e9

N, S = map(int,input().split())
nums = list(map(int, input().split()))

ans, cur, l, r = INF, nums[0], 0, 0

while r < N:
    if cur >= S:
        ans = min(ans, r - l + 1)

        if l < r:
            cur -= nums[l]
            l += 1
        else:
            r += 1
            if r < N:
                cur += nums[r]
    else:
        r += 1
        if r < N:
            cur += nums[r]

print(ans if ans < INF else 0)