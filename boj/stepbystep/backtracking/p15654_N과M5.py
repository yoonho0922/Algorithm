def sol(depth):
    if depth==M:
        for i in out:
            print(nums[i], end=' ')
        print()

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            out.append(i)
            sol(depth+1)
            visited[i] = 0
            out.pop()

N, M = map(int, input().split())
nums = list(map(int, input().split()))
visited = [0]*N
out = []

nums.sort()
sol(0)