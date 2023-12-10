def sol(depth, x):
    if depth == M:
        for i in out:
            print(nums[i], end=' ')
        print()
        return

    for i in range(x, len(nums)):
        out.append(i)
        sol(depth+1, i)
        out.pop()



N, M = map(int, input().split())
nums = list(map(int, input().split()))
out = []

nums = list(set(nums))
nums.sort()
sol(0, 0)