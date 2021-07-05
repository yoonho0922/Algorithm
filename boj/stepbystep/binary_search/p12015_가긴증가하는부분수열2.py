def search(num, left, right):
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        if sequence[mid] >= num:
            right = mid - 1
            ans = mid
        else:
            left = mid + 1

    return ans

N = int(input())
nums = list(map(int, input().split()))

sequence = [0]

for num in nums:
    if num > sequence[-1]:
        sequence.append(num)
    else:
        i = search(num, 0, len(sequence))
        sequence[i] = num

print(len(sequence)-1)