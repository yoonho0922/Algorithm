# https://www.acmicpc.net/problem/1918

S = list(input())
stack=[]
res=''

for c in S:
    if c.isalpha():
        res += c
    else:
        if c == '(':
            stack.append(c)
        elif c in ['*','/']:
            while stack and stack[-1] in ['*','/']:
                res += stack.pop()
            stack.append(c)
        elif c in ['+','-']:
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()

while stack:
    res += stack.pop()

print(res)