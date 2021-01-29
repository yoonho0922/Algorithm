import sys
readline = sys.stdin.readline

N = int(readline())
cards = list(map(int, readline().split()))
M = int(readline())
nums = list(map(int, readline().split()))

count = {}

for c in cards:
    if count.get(c):
        count[c] += 1
    else:
        count[c] = 1

for num in nums:
    # search(num, 0, len(cards)-1)
    if count.get(num):
        print(count[num], end=' ')
    else:
        print(0, end=' ')