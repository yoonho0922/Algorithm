N = int(input())
nums = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))
nums.sort()

def search(left, right, target):
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return 1
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return 0

for target in targets:
    print(search(0, N-1, target))
