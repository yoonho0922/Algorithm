# https://www.acmicpc.net/problem/17266
# 어두운 굴다리

N = int(input())
M = int(input())
locations = list(map(int, input().split()))


def check_bright(height):
    # 양 끝을 비출 수 있는지 확인
    if height < locations[0] or height < (N - locations[-1]):
        return False

    # 가로등 사이를 비출 수 있는지 확인
    for i in range(len(locations) - 1):
        if height < (locations[i+1]-locations[i])/2:
            return False

    return True


def binary_search(start, end):
    if start > end:
        return None

    mid = (start+end)//2
    bright = check_bright(mid)

    if bright:
        next = binary_search(start, mid-1)
        if next is None:
            return mid
        else:
            return next
    else:
        return binary_search(mid+1, end)


print(binary_search(1, N))