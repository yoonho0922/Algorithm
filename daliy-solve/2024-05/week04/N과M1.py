# https://www.acmicpc.net/problem/15649


def backtrack(nums, depth):
    if depth == M:
        print(' '.join(map(str,nums)))
        return

    for i in range(1, N+1):
        if i not in nums:
            backtrack(nums + [i], depth + 1)

N, M = map(int, input().split())

backtrack([], 0)