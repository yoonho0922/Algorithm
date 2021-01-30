import sys
readline = sys.stdin.readline

def search(target, left, right):
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            print(1)
            return
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1

    print(0)

T = int(readline())

for _ in range(T):
    N = int(readline())
    nums = list(map(int, readline().split()))
    M = int(readline())
    targets = list(map(int, readline().split()))

    nums.sort()

    for target in targets:
        search(target, 0, len(nums) - 1)
