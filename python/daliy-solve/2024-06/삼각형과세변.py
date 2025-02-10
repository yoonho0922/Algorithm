# https://www.acmicpc.net/problem/5073

while True:
    sides = list(map(int,input().split()))
    sides.sort()

    if sides == [0,0,0]:
        exit()
    elif sides[2] >= sides[0] + sides[1]:
        print('Invalid')
    elif sides == [sides[0], sides[0], sides[0]]:
        print('Equilateral')
    elif sides[0] == sides[1] or sides[1] == sides[2]:
        print('Isosceles')
    else:
        print('Scalene')