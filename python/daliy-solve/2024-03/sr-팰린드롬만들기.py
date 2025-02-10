# https://www.acmicpc.net/problem/1213

import collections

S = sorted(input())

counter = list(collections.Counter(S).items())

odd_chars = [map for map in counter if map[1]%2==1]
even_chars = [map for map in counter if map[1]%2==0]

# 홀수 개인 문자가 두 개 이상이면 팰린드롬을 만들 수 없음
if len(odd_chars) > 1:
    print('I\'m Sorry Hansoo')
    exit()

front = ''.join([char[0]*(char[1]//2) for char in counter])
mid = odd_chars[0][0][0] if odd_chars else ''
back = ''.join(front[::-1])

print(front+mid+back)