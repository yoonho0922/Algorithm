# https://www.acmicpc.net/problem/2668


def dfs(cur, target):
    if nums[cur] == target:
        result.append(target)
        visited[cur] = True
        return True

    nxt = nums[cur]
    if not visited[nxt]:
        visited[cur] = True
        if dfs(nxt, target):
            result.append(nxt)
            return True
        else:
            visited[cur] = False


N = int(input())
nums = [0] + [int(input()) for _ in range(N)]

result = []
visited = [False] * (N + 1)

for i in range(1, N + 1):
    dfs(i, i)

print(len(result))
for r in sorted(result):
    print(r)