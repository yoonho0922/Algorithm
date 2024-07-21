# https://www.acmicpc.net/problem/9613


def get_gcd(x,y):
    while x%y != 0:
        tmp = x%y
        x = y
        y = tmp
    return y

T = int(input())
for _ in range(T):
    nums = list(map(int, input().split()))[1:]

    gcd_sum = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            gcd_sum += get_gcd(nums[i], nums[j])
    print(gcd_sum)