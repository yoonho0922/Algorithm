import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
trees = list(map(int, readline().split()))

left, right, res = 0, max(trees) - 1, 0

while left <= right:
    mid = (left + right) // 2
    sum_tree = 0
    # 현재 높이에서 가져갈 수 있는 나무 길이를 구함
    for i in range(N):
        if mid < trees[i]:
            sum_tree += trees[i] - mid

    if sum_tree >= M:
        res = mid
        left = mid + 1
    elif sum_tree < M:
        right = mid - 1

print(right)