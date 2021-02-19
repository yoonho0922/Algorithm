import sys
readline = sys.stdin.readline

T = int(readline())

for _ in range(T):
    N = int(readline())
    nums = list(map(int, readline().split()))

    profit = 0
    max = 0

    for i in range(N - 1, -1, -1):
        if nums[i] > max:
            max = nums[i]
        else:
            profit += max - nums[i]

    print(profit)