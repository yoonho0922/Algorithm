def binarySearch(target, left, end):
    if left > end:
        return False

    mid = (left + end) // 2

    if m_list[mid] == target:
        return mid
    elif m_list[mid] > target:
        end = mid - 1
    else:
        left = mid + 1

    return binarySearch(target, left, end)

target = 27
m_list = [30, 94, 27, 92, 21, 37, 25, 47, 25, 53, 98, 19, 32, 32, 7]
length = len(m_list)

m_list.sort()
left = 0
right = length-1

print(binarySearch(target,0,right))