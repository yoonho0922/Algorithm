import sys
readline = sys.stdin.readline
K = int(readline())
nums = []
for _ in range(K):
    num = int(readline())
    if num == 0 and len(nums) > 0:
        nums.pop()
    else:
        nums.append(num)
print(sum(nums))