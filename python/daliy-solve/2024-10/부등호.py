# https://www.acmicpc.net/problem/2529

def valid(prev: int, now: int, sign: str):
    if sign == '<':
        return prev < now
    else:
        return prev > now

def dfs(index: int, num: str):
    if index == N + 1:
        global max_num
        global min_num
        if int(num) > int(max_num):
            max_num = num
        if int(num) < int(min_num):
            min_num = num
        return

    for i in range(10):
        if visited[i]:
            continue
        if 0 < index:
            prev = int(num[index - 1])
            sign = signs[index - 1]
            # 다음에 들어갈 수가 부등호에 부합하는지 검사
            if not valid(prev, i, sign):
                continue

        visited[i] = True
        dfs(index + 1, num + str(i))
        visited[i] = False


N = int(input())
signs = list(input().split())

max_num, min_num = '0', '9' * 10
visited = [False] * 10
dfs(0, '')

print(max_num)
print(min_num)
