# 부품 찾기

import sys
readline = sys.stdin.readline

N = int(readline())
items = list(map(int, input().split()))

items.sort()


def binary_search(target, start, end):
    if start>end:
        return None

    mid = (start+end)//2

    if items[mid] == target:
        return mid
    if items[mid] > target:
        return binary_search(target, start, mid-1)
    if items[mid] < target:
        return binary_search(target, mid+1, end)

M = int(readline())
targets = list(map(int, input().split()))

for i in range(M):
    if binary_search(targets[i], 0, len(items)) is None:
        print("no")
    else:
        print("yes")