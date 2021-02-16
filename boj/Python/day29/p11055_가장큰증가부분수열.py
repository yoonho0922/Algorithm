import sys
readline = sys.stdin.readline

N = int(readline())
nums = list(map(int, readline().split()))

d = [0] * N
d[0] = nums[0]

for i in range(1, N):
    li = []
    for j in range(i):
        if nums[j] < nums[i]:
            li.append(d[j])
    d[i] = nums[i] + max(li)

print(max(d))