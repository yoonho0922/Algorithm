import sys
readline = sys.stdin.readline

N = int(readline())
nums = []
for _ in range(N):
    nums.append(int(readline()))

gaps = []
for i in range(N-1):
    gaps.append(abs(nums[i]-nums[i+1]))

mg = min(gaps)
divs = []
for i in range(2, mg+1):
    if mg%i == 0:
        divs.append(i)

for div in divs:
    for gap in gaps:
        if gap%div != 0:
            break
    else:
        print(div, end=' ')