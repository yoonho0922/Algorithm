# https://www.acmicpc.net/problem/15651


def backtrack(nums, depth):
    if depth == M:
        print(' '.join(map(str,nums)))
        return

    for i in range(1, N+1):
        backtrack(nums + [i], depth + 1)

N, M = map(int, input().split())

backtrack([], 0)