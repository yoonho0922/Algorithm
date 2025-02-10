# https://www.acmicpc.net/problem/13706

N = int(input())

left, right = 1, N

result = 0

while left <= right:
    mid = (left+right)//2

    if mid * mid >= N:
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)