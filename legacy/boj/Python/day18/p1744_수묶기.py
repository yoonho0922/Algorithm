import sys
readline = sys.stdin.readline

N = int(readline())
nums = []
for _ in range(N):
    nums.append(int(readline()))

nums.sort()
p_index = N

for i in range(N):
    if nums[i] > 0:
        p_index = i
        break

result = 0

# 0이하의 정수는 절댓값이 큰거 끼리 곱함
for i in range(0, p_index, 2):
    if i+1 >= p_index or i+1 >= N:
        result += nums[i]
    else:
        result += nums[i] * nums[i+1]

# 양수는 절댓값이 큰거 끼리 곱하되 1은 예외처리함
for i in range(N-1, p_index-1, -2):
    if i-1 <= p_index-1 or i-1 < 0:
        result += nums[i]
    elif nums[i-1] == 1:
        result += nums[i] + 1
    else:
        result += nums[i] * nums[i-1]

print(result)