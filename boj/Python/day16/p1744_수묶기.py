import sys
readline = sys.stdin.readline

N = int(readline())
nums = []
for _ in range(N):
    nums.append(int(readline()))

nums.sort()
result = 0
n_end, p_start = -1, N

# 음수 끝 인덱스, 양수 시작 인덱스 탐색
for i in range(N):
    if nums[i] < 0:
        n_end = i
    elif nums[i] > 0:
        p_start = i
        break

# 절댓값이 큰 음수 끼리 묶음
for i in range(0, n_end+1, 2):
    if i+1 > N-1 or nums[i+1] > 0:
        result += nums[i]
        break
    result += nums[i] * nums[i+1]

# 절댓값이 큰 양수 끼리 묶음
for i in range(N-1, p_start-1, -2):
    if i-1 < 0 or nums[i-1] <= 0:
        result += nums[i]
        break
    # 예외 1은 묶는 것 보다 따로 더하는게 큼
    if nums[i] == 1 or nums[i-1] == 1:
        result += nums[i] + 1
        continue

    result += nums[i] * nums[i-1]

print(result)