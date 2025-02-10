# https://www.acmicpc.net/problem/15654


def backtrack(res, depth):
    if depth == M:
        print(' '.join(map(str, res)))

    for num in nums:
        if num not in res:
            backtrack(res + [num], depth+1)

N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

backtrack([], 0)