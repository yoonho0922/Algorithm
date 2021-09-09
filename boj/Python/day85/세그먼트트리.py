def init(start, end, node):
    if start==end:
        tree[node] = a[start]
        return tree[node]

    mid = (start+end)//2
    tree[node] = init(start, mid, node*2) + init(mid+1, end, node*2+1)
    return tree[node]

# s, e : 시작, 끝 인덱스 (가변)
# l, r : 구간 합을 구하고자하는 범위 (불변)
def sumTree(s, e, node, l, r,depth=0):
    # print("ㄴ"*depth, s, e, node)
    # 완전히 범위 밖인 경우
    if l>e or r<s:
        return 0
    # s e 모두 범위 안인 경우
    if l<=s and e<=r:
        # print("return ", node)
        return tree[node]

    mid = (s+e)//2
    return sumTree(s,mid,node*2,l, r, depth+1) + sumTree(mid+1,e,node*2+1,l,r,depth+1)

def update(s, e, node, target, value):
    # 범위 밖인 경우
    if not (s <= target <= e): # s > target or target > e
        return

    # 범위 안이면 내려가며 다른 원소도 갱신
    tree[node] += value

    if s==e:
        return

    mid = (s+e)//2

    update(s, mid, node*2, target, value)
    update(mid+1, e, node*2+1, target, value)

N = 12
a = [1,9,3,8,4,5,5,9,10,3,4,5]
tree = [0]*N*4

init(0, N-1, 1) # 트리의 인덱스는 1부터 시작 (그래야 *2 했을 때 왼쪽 자식을 가리킴)
print(tree)
print(sumTree(0,N-1,1,0,2)) # 구간의 인덱스는 0부터 시작
print(sumTree(0,N-1,1,3,8))

update(0,N-1, 1, 5, -5) # 인덱스 5의 원소를 -5 만큼 수
print(sumTree(0,N-1,1,3,8))