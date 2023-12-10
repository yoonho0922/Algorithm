N = int(input())
nums = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

count = {}
for num in nums:
    if count.get(num):
        count[num] += 1
    else:
        count[num] = 1

for t in targets:
    if count.get(t):
        print(count[t], end= ' ')
    else:
        print(0, end= ' ')