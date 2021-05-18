import sys
from collections import Counter
readline = sys.stdin.readline

N = int(readline())
nums = []
for _ in range(N):
    num = int(readline())
    nums.append(num)

def getMode():
    if N==1:
        return nums[0]
    counter = Counter(nums)
    order = counter.most_common()
    order.sort(key=lambda x:(-x[1], x[0]))
    if order[0][1] == order[1][1]:
        return order[1][0]
    return order[0][0]


print(round(sum(nums)/N))
print(sorted(nums)[N//2])
print(getMode())
print(max(nums)-min(nums))
