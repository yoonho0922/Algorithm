from itertools import combinations


def backtrack(start, total):
    if total > 0:
        checked[total] = True

    for i in range(start, N):
        backtrack(i+1, total + nums[i])
        backtrack(i+1, total - nums[i])


N = int(input())
nums = list(map(int, input().split()))

S = sum(nums)

checked = [False] * (S+1)

backtrack(0, 0)

ans = 0

# print(checked)

for i in range(1, S+1):
    if not checked[i]:
        ans += 1

print(ans)