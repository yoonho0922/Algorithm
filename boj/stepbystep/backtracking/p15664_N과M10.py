def sol(depth, x):
    if depth == M:
        for i in out:
            print(nums[i], end=' ')
        print()

    prev = 0

    for i in range(x, N):
        if not visited[i] and prev != nums[i]:
            prev = nums[i]

            visited[i] = 1
            out.append(i)
            sol(depth+1, i)
            visited[i] = 0
            out.pop()


N, M = map(int, input().split())
nums = list(map(int, input().split()))
out = []
visited=[0]*N

nums.sort()
sol(0, 0)