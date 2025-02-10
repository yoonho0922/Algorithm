# https://www.acmicpc.net/problem/20115

N = int(input())
drinks = list(map(int, input().split()))

drinks.sort(reverse=True)

answer = drinks[0]

for drink in drinks[1:]:
    answer += drink / 2

if answer == int(answer):
    print(int(answer))
else:
    print(answer)