# https://www.acmicpc.net/problem/4158

import sys
readline = sys.stdin.readline

def isPresent(A, x):
    left, right = 0, len(A)-1

    while left <= right:
        mid = (left + right)//2

        if A[mid] == x:
            return True

        if A[mid] < x:
            left = mid + 1
        else:
            right = mid -1

while True:
    N, M = map(int, input().split())
    if [N, M] == [0,0]:
        break

    A = list(int(input()) for _ in range(N))

    A.sort()
    ans = 0

    for _ in range(M):
        x = int(input())

        if isPresent(A, x):
            ans += 1

    print(ans)
