# 떡볶이 떡 만들기

N, M = map(int, input().split())
items = list(map(int, input().split()))


def get_total(cutting_height):
    total = 0
    for item in items:
        if item > cutting_height:
            total += item - cutting_height
    return total


def binary_search(target_total, start, end):
    if start > end:
        return None

    mid = (start+end)//2
    total = get_total(mid)

    if total == target_total:
        return mid
    if total < target_total:
        # total 늘리기
        return binary_search(target_total, start, mid - 1)
    if total > target_total:
        # total 줄이기, 줄였는데 맞는 크기가 없다면 현재 높이 반환
        result = binary_search(target_total, mid + 1, end)

        if result is None:
            return mid
        else:
            return result


MAX_HEIGHT = 1000000000
print (binary_search(M, 1, MAX_HEIGHT))