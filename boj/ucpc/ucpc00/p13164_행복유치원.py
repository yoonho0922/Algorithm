N, K = map(int ,input().split())
nums = list(map(int, input().split()))
gaps = []
for i in range(N-1):
    gaps.append(nums[i+1]-nums[i])

gaps.sort()
print(sum(gaps[:N-1-(K-1)]))