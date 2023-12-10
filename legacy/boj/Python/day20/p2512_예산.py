import sys
readline = sys.stdin.readline

N = int(readline())
nums = list(map(int, readline().split()))
M = int(readline())

nums.sort()

left, right, ans = 1, max(nums), 0

while left <= right:
    mid = (left + right) // 2
    budget = M

    for num in nums:
        if num > mid:
            budget -= mid
        else:
            budget -= num

    if budget >= 0:
        ans = mid
        left = mid + 1
    else:
        right = mid -1

print(ans)