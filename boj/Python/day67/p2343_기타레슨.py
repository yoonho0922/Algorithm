def check(size):
    count = 1  # blue-ray count
    ts = 0  # this size

    for l in lessons:
        if count > M:
            break
        if ts + l <= size:
            ts += l
        else:
            count += 1
            ts = l

    return False if count > M else True

def binary_search(ans, left, right):
    while left <= right:
        mid = (left + right) // 2

        if check(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans

N, M = map(int, input().split())
lessons = list(map(int, input().split()))

print(binary_search(0, 1, sum(lessons)))