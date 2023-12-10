import sys
sys.setrecursionlimit(9999999)
readline = sys.stdin.readline

def init(s, e, node):
    if s==e:
        tree[node] = nums[s]
        return tree[node]

    mid = (s+e)//2
    tree[node] = init(s, mid, node*2) + init(mid+1, e, node*2+1)
    return tree[node]

def sumTree(s, e, node, l, r):
    # 완전히 범위를 벗어난 경우
    if s>r or e<l:
        return 0

    # s, e 가 모두 범위 내인 경우
    if l<=s and e<=r:
        return tree[node]

    mid = (s+e)//2
    return sumTree(s, mid, node*2, l, r) + sumTree(mid+1, e, node*2+1, l, r)


N, M = map(int, readline().split())
nums = list(map(int, readline().split()))

tree = [0]*N*4
init(0, N-1, 1)

for _ in range(M):
    a, b = map(int, readline().split())
    print(sumTree(0, N-1, 1, a-1, b-1))