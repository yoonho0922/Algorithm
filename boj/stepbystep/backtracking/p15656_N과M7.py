def sol(depth):
    if depth==M:
        for i in out:
            print(nums[i], end=' ')
        print()
        return

    for i in range(N):
        if not visited[i]:
            out.append(i)
            sol(depth+1)
            out.pop()


N, M = map(int, input().split())
nums = list(map(int, input().split()))
visited = [0]*N
out = []

nums.sort()
sol(0)