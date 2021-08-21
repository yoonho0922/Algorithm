# 노드의 부모를 재귀적으로 구함
def getParent(parent, x):
    if parent[x]==x:
        return x
    parent[x] = getParent(parent, parent[x])
    return parent[x]

# 각 부모 노드를 합침 - 부모의 값이 변경됨
def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

# 같은 부모를 가지는지 확인
def findParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    return 1 if a==b else 0

parent = [0]*11
for i in range(1,9):
    parent[i] = i

unionParent(parent, 1, 2)
unionParent(parent, 2, 3)
unionParent(parent, 4, 5)
unionParent(parent, 5, 6)
unionParent(parent, 1, 6)

print(findParent(parent, 3,4))
print(findParent(parent, 1,3))