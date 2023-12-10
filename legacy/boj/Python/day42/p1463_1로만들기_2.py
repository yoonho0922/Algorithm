N = int(input())
d = [0] * (N+1)

for i in range(2, N+1):
    nums = []
    nums.append(d[i-1] + 1)
    if i%2 == 0: nums.append(d[i//2] + 1)
    if i%3 == 0: nums.append(d[i//3] + 1)
    d[i] = min(nums)
print(d[N])