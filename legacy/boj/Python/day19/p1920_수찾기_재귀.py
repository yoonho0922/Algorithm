import sys
readline = sys.stdin.readline

def binarySearch(target, start, end):
    if start > end:
        return False

    mid = (start + end) // 2

    if nums[mid] == target:
        return True
    elif nums[mid] > target:
        end = mid - 1
    else:
        start = mid + 1

    return binarySearch(target, start, end)

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