N = int(input())
nums = list(map(int, input().split()))
budget = int(input())
num_sum = sum(nums)

def inspect(limit):
    total = 0
    for num in nums:
        if num > limit:
            total += limit
        else:
            total += num
    return total

def search():
    ans, left, right = 0, 0, 100001
    while left <= right:
        mid = (left + right) // 2
        total = inspect(mid)
        if total > budget:
            right = mid - 1
        elif total <= budget:
            if total == num_sum:
                return max(nums)
            left = mid + 1
            ans = mid

    return ans

print(search())