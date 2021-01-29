import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
trees = list(map(int, readline().split()))

left, right, ans = 0, max(trees) - 1, 0

while left <= right:
    mid = (left + right) // 2
    sum_tree = 0

    for i in trees:
        if i > mid:
            sum_tree += i - mid

    # 길이가 부족하면 높이를 줄여야함
    if sum_tree < M:
        right = mid - 1
    # 길이가 충분하면 높이를 올림
    else:
        ans = mid
        left = mid + 1

print(ans)