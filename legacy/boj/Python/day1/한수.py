import sys

N = int(sys.stdin.readline())

hansu = 0

for i in range(1,N+1):
    if(i <100):
        hansu += 1
    else:
        nums = list(map(int, str(i)))
        if(nums[1]*2 == nums[0]+nums[2]):
            hansu += 1

print(hansu)

