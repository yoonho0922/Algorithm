# 부모를 재귀적으로 구하기
def getParent(parent, x):
    if parent[x]==x:
        return x
    parent[x] = getParent(parent, parent[x])
    return parent[x]

# 노드를 합치고 부모를 업데이트
def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a<b:
        parent[a] = b
    else:
        parent[b] = a

# 같은 부모인지 확인
def findParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    return True if a==b else False

G = []

parent = [0]*11
for i in range(1, 11):
    parent[i] = i

G.append([1,7,12])
G.append([1,4,28])
G.append([1,2,67])
G.append([1,5,17])
G.append([2,4,24])
G.append([2,5,62])
G.append([3,5,20])
G.append([3,6,37])
G.append([4,7,13])
G.append([5,6,45])
G.append([5,7,73])

G.sort(key=lambda x:x[2])

sum = 0

for v1, v2, c in G:
    if not findParent(parent, v1, v2):
        sum+=c
        unionParent(parent, v1, v2)

print(sum)
