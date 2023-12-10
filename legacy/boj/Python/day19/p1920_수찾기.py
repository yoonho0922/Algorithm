import sys
readline = sys.stdin.readline

def binarySearch(target, left, right):

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False

N = int(readline())
nums = list(map(int, readline().split()))
M = int(readline())
targets = list(map(int, readline().split()))

nums.sort()

for i in targets:
    if binarySearch(i, 0, len(nums)-1):
        print(1)
    else:
        print(0)