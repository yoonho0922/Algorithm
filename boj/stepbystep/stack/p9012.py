import sys
readline = sys.stdin.readline

def sol(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(1)
        elif s[i] == ')':
            if len(stack)>0:
                stack.pop()
            else:
                return 'NO'
    return 'YES' if len(stack)==0 else 'NO'


T = int(readline())
for _ in range(T):
    S = input()
    print(sol(S))
