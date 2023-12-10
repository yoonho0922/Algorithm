import sys
readline = sys.stdin.readline

def sol(s):
    stack = []

    for i in range(len(s)):
        if s[i]=='(':
            stack.append('(')
        elif s[i]=='[':
            stack.append('[')
        elif s[i]==')':
            if len(stack)==0 or stack[-1]!='(':
                return 'no'
            stack.pop()
        elif s[i]==']':
            if len(stack)==0 or stack[-1]!='[':
                return 'no'
            stack.pop()

    return 'yes' if len(stack)==0 else 'no'


while True:
    S = readline()
    if S[0]=='.':
        break

    print(sol(S))