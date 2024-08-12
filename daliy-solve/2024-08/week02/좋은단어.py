# https://www.acmicpc.net/problem/3986

def check(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return not stack


N = int(input())
ans = 0
for _ in range(N):
    s = input()
    if check(s):
        ans += 1
print(ans)