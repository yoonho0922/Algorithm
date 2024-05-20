# https://www.acmicpc.net/problem/15650


def backtrack(nums, depth, start):
    if depth == M:
        print(' '.join(map(str,nums)))
        return

    for i in range(start, N+1):
        backtrack(nums + [i], depth + 1, i+1)

N, M = map(int, input().split())

backtrack([], 0, 1)