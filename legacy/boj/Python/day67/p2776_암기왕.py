T = int(input())

for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    M = int(input())
    targets = list(map(int, input().split()))
    dictionary = {}

    for num in nums:
        dictionary[num] = 1

    for target in targets:
        if dictionary.get(target):
            print(1)
        else:
            print(0)