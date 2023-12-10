import sys
readline = sys.stdin.readline

def search(target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] == target:
            print(1, end=' ')
            return
        elif cards[mid] > target:
            right = mid - 1
        elif cards[mid] < target:
            left = mid + 1

    print(0, end=' ')

N = int(readline())
cards = list(map(int, readline().split()))
M = int(readline())
nums = list(map(int, readline().split()))

cards.sort()

for num in nums:
    search(num, 0, len(cards)-1)