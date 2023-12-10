import itertools

N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))
opList = []

for i in range(4):
    for _ in range(ops[i]):
        opList.append(i)

max_val = -1000000000
min_val = 1000000000

permu = set(list(itertools.permutations(opList)))

for p in permu:
    result = nums[0]

    for i in range(N - 1):
        if p[i] == 0:
            result += nums[i+1]
        elif p[i] == 1:
            result -= nums[i+1]
        elif p[i] == 2:
            result *= nums[i+1]
        elif p[i] == 3:
            if result % nums[i+1] != 0 and result//nums[i+1] < 0:
                result //= nums[i + 1]
                result += 1
            else:
                result //= nums[i + 1]

    max_val = max(result, max_val)
    min_val = min(result, min_val)

print(max_val)
print(min_val)
