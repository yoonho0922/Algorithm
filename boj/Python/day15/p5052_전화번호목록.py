import sys
readline = sys.stdin.readline

def inspect(cur, next):
    for i in range(len(cur)):
        if next[i] != cur[i]:
            return False
    # 접두어가 다른 번호와 일치
    return True

def solve():
    for i in range(N-1):
        if inspect(nums[i], nums[i+1]):
            return 'NO'
    return 'YES'


T = int(readline())
for _ in range(T):

    N = int(readline())
    nums = []
    for _ in range(N):
        num = list(map(int, readline().strip()))
        nums.append(num)

    nums.sort()
    print(solve())