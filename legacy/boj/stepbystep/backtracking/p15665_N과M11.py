def sol(depth):
    if depth == M:
        for i in out:
            print(nums[i], end=' ')
        print()
        return

    for i in range(len(nums)):
        out.append(i)
        sol(depth+1)
        out.pop()


N, M = map(int, input().split())
nums = list(map(int, input().split()))
out = []

nums = list(set(nums))
nums.sort()
sol(0)