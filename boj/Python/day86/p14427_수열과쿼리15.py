import sys
sys.setrecursionlimit(9999999)
readline = sys.stdin.readline

def minIdx(x, y):
    if nums[x] == nums[y]:
        return min(x, y)
    if nums[x] < nums[y]:
        return x
    return y

def init(s, e, node):
    if s==e:
        tree[node] = s
        return tree[node]

    mid = (s+e)//2
    tree[node] = minIdx(init(s, mid, node*2), init(mid+1, e, node*2+1))
    return tree[node]

def update(s, e, node, idx):
    if not(s<=idx<=e) or s==e:
        return tree[node]

    mid = (s+e)//2
    tree[node] = minIdx(update(s, mid, node*2, idx), update(mid+1, e, node*2+1, idx))
    return tree[node]

N = int(readline())
nums = list(map(int, readline().split()))

tree = [0]*N*4
init(0, N-1, 1)

M = int(readline())
for _ in range(M):
    query = list(readline().split())

    if query[0] == '1':
        idx, val = map(int, query[1:])
        nums[idx-1] = val
        update(0, N-1, 1, idx-1)
    elif query[0] == '2':
        print(tree[1]+1)