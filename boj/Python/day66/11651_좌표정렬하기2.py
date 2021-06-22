N = int(input())
nums = []
for _ in range(N):
    nums.append(list(map(int, input().split())))
nums.sort(key=lambda x : (x[1], x[0]))
for num in nums:
    print(*num)
