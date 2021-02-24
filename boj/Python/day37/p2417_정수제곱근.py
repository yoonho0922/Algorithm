N = int(input())
ans, left, right = 0, 0, pow(2,63)
while left <= right:
    mid = (left + right) // 2
    a = pow(mid, 2)
    if a >= N:
        right = mid - 1
        ans = mid
    elif a < N:
        left = mid + 1
print(ans)