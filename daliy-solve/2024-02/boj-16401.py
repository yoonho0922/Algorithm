# https://www.acmicpc.net/problem/16401
# 과자 나눠주기

def get_divided_snack_count(height):
    count = 0

    for snack in snacks:
        count += snack//height

    return count


def binary_search(target_count):
    result, start, end = 0, 1, max(snacks)

    while start <= end:
        mid = (start+end)//2
        count = get_divided_snack_count(mid)

        if count >= target_count:
            # 틀린 조건
            # if count == target_count:
            #     result = mid
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result

M, N = map(int, input().split())
snacks = list(map(int, input().split()))

print(binary_search(M))