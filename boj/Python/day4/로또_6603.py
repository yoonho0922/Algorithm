import sys
input = sys.stdin.readline

def dfs(s, d): # start, depth

    if d == 6:
        for i in range(6):
            print(C[i], end=' ')
        print()
        return

    for i in range(s, len(nums)):
        C[d] = nums[i]
        dfs(i+1, d+1)

C = [0]*12

while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    nums.pop(0)
    dfs(0,0)
    print()
