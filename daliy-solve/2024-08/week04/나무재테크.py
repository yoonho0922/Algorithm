# https://www.acmicpc.net/problem/16235

from collections import deque

dy = [1,1,1,0,0,-1,-1,-1]
dx = [-1,0,1,-1,1,-1,0,1]

def supply(grid, A):
    # 양분을 재공급한다
    for r in range(N):
        for c in range(N):
            grid[r][c] += A[r][c]

def multiply(trees):
    # 나무의 나이가 5의 배수라면 나무가 주변 8 방향으로 증식한다
    parent_trees = []
    for r in range(N):
        for c in range(N):
            for age in trees[r][c]:
                if age % 5 == 0:
                    parent_trees.append([r,c])
    for r, c in parent_trees:
        for i in range(8):
            ny = r + dy[i]
            nx = c + dx[i]
            if 0<=nx<N and 0<=ny<N:
                trees[ny][nx].appendleft(1)

def growthOrDeath(grid, trees):
    # 어린 나무 부터 나이 만큼 양분을 먹고 나이를 1 먹는다.
    # 나이 만큼 양분이 없다면 즉시 죽는다.
    # 죽은 나무는 즉시 양분이 된다.
    for r in range(N):
        for c in range(N):
            if not trees[r][c]:
                continue
            # print('before', grid[r][c], trees[r][c])
            added = 0
            for _ in range(len(trees[r][c])):
                age = trees[r][c].popleft()
                if grid[r][c] >= age:
                    # 나무가 성장한다
                    grid[r][c] -= age
                    trees[r][c].append(age + 1)
                else:
                    # 나무가 양분이 된다
                    added += age // 2
            grid[r][c] += added
            # print('after', grid[r][c], trees[r][c])
            # print()


N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
trees = [[deque() for _ in range(N)] for _ in range(N)]


# 입력으로 주어지는 나무의 위치는 모두 서로 다름
for _ in range(M):
    r, c, age = map(int, input().split())
    trees[r-1][c-1].append(age)

# 양분이 있는 땅
grid = [[5]*N for _ in range(N)]

for _ in range(K):
    growthOrDeath(grid, trees) # 봄, 여름 : 양분을 먹고 나이가 들거나 죽는다
    multiply(trees) # 가을 : 나무가 증식한다
    supply(grid, A) # 겨울 : 양분을 재공급한다

ans = 0
for r in range(N):
    for c in range(N):
        ans += len(trees[r][c])
print(ans)