# https://www.acmicpc.net/problem/3273

N = int(input())
A = list(map(int, input().split()))
X = int(input())

A.sort()

l, r = 0, N-1
ans = 0

while l < r:
    if A[l] + A[r] == X:
        ans += 1
        l += 1
        r -= 1
    elif A[l] + A[r] < X:
        l += 1
    else:
        r -= 1

print(ans)