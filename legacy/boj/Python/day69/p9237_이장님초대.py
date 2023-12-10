N = int(input())
trees = list(map(int, input().split()))
trees.sort(reverse=True)
yard = []
ans = 1

for i in range(N):
    plant = i+2
    height = trees[i]
    yard.append(plant + height)

print(max(yard))