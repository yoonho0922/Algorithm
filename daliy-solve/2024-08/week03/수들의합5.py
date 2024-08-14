# https://www.acmicpc.net/problem/2018

N = int(input())
left,right = N, N
ans = 0

while left > 0:
    res = (left + right) * (right - left + 1) // 2

    if res == N:
        ans += 1
        right -= 1
        left -= 1
    elif res < N:
        left -= 1
    else:
        right -= 1

print(ans)