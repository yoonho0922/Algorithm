N, M = map(int, input().split())
trees = list(map(int, input().split()))

def cutting(height):
    cut = 0
    for tree in trees:
        if tree > height:
            cut += tree - height
    return cut

def search(left, right, target):
    ans = 0
    while left <= right:
        mid = (left+right) // 2
        cut = cutting(mid)
        if cut >= target:
            left = mid + 1
            ans = mid
        elif cut < target:
            right = mid - 1
    return ans

print(search(0, max(trees), M))