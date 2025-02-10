# https://www.acmicpc.net/problem/17615

def cut(s, target):
    start = 0
    for ch in s:
        if ch == target:
            start += 1
        else:
            break
    return s[start:]

N = int(input())
balls = input()
reversed_balls = balls[::-1]

# red left
answer = cut(balls, 'R').count('R')

# red right
answer = min(answer, cut(reversed_balls, 'R').count('R'))

# blue left
answer = min(answer, cut(balls, 'B').count('B'))

# blue right
answer = min(answer, cut(reversed_balls, 'B').count('B'))

print(answer)