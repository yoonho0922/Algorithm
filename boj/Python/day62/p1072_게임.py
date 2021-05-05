X, Y = map(int, input().split())
Z = Y*100//X

def search():
    ans, left, right = -1, 0, X
    while left <= right:
        mid = (left+right)//2
        update = (Y+mid)*100//(X+mid)
        if update > Z:
            right = mid-1
            ans = mid
        else:
            left = mid+1
    return ans

print(search())
