import sys
readline = sys.stdin.readline

N = int(readline())
nums = []
for _ in range(N):
    nums.append(int(readline()))
nums.sort()
for num in nums:
    print(num)