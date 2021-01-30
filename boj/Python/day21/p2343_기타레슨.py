import sys
readline = sys.stdin.readline

def inspect(size):

    count = 1
    cur_size = 0

    for l in lessons:
        if cur_size + l <= size:
            cur_size += l
        else:
            cur_size = l
            count += 1

    return count


N, M = map(int, readline().split())
lessons = list(map(int, readline().split()))

left, right, ans = max(lessons), sum(lessons), 0

while left <= right:
    mid = (left + right) // 2
    print(mid, inspect(mid))
    if inspect(mid) <= M:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)