N = int(input())
nums = list(map(int, input().split()))

sn = sorted(nums)
dict_nums = {}
i, prev = 0, sn[0]

for num in sn:
    if prev != num:
        i += 1
        prev = num
    dict_nums[num] = i

for num in nums:
    print(dict_nums[num], end=' ')