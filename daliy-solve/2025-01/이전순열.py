# https://www.acmicpc.net/problem/10973

def is_asc(nums):
    for  i in range(len(nums) - 1):
        if not (nums[i] < nums[i+1]):
            return False
    return True

def get_lower(maximum, sub_nums):
    result = 0
    for num in sub_nums:
        if maximum > num > result:
            result = num
    return result

N = int(input())
nums = list(map(int, input().split()))

answer = [-1]

for i in range(N-1, -1, -1):

    if is_asc(nums[i:]):
        continue
    else:
        # nums[i]는 오름차순을 깨는 수
        # 부분 배열에서 nums[i]와 nums[i]보다 하나 작은 수의 위치를 교체함
        for j in range(N-1, i, -1):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break
        # 오름차순이 아닌 배열에서 nums[i]보다 하나 작은 수가 맨 앞으로 가고, 그 뒤의 배열이 최대값이면 이전 순열이다.
        answer = nums[:i+1] + sorted(nums[i+1:], reverse=True)
        break

print(*answer)