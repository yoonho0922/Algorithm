N = int(input())
nums = list(map(int, input().split()))
budget = int(input())

def inspect(limit):
    total = 0
    for num in nums:
        if num > limit:
            total += limit
        else:
            total += num
    return total <= budget

def search():
    ans, left, right = 0, 0, max(nums)
    while left <= right:
        mid = (left + right) // 2
        if inspect(mid):
            left = mid+1
            ans = mid
        else:
            right = mid-1

    return ans

print(search())