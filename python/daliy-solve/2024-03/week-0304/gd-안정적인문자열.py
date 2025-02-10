# https://www.acmicpc.net/problem/4889

import math
import sys
readline = sys.stdin.readline


def solution(S):
    stack = []

    for c in S:
        if c == '{':
            stack.append('{')
        if c == '}':
            if len(stack)==0 or stack[-1] != '{':
                stack.append('}')
            else:
                stack.pop()


    a = stack.count('{')
    b = stack.count('}')

    return int(math.ceil(a/2) + math.ceil(b/2))

case = 1

while True:
    S = str(readline().rstrip())

    if S.find('-') != -1:
        break

    print(f'{case}. {solution(S)}')
    case += 1
