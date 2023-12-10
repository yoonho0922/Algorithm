def sol(depth):
    if depth == M:
        for i in out:
            print(nums[i], end=' ')
        print()

    for i in range(N):
        if i > 0 and not visited[i-1] and nums[i-1] == nums[i]:
            continue
        if not visited[i]:
            visited[i] = 1
            out.append(i)
            sol(depth+1)
            visited[i] = 0
            out.pop()



N, M = map(int, input().split())
nums = list(map(int, input().split()))
out = []
visited=[0]*N

nums.sort()
sol(0)