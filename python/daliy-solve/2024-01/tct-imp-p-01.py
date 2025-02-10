# 왕실의 나이트

place = input()

horizon = ['a','b','c','d','e','f','g','h']
# vertical = 1...8

dy = [2,2,-2,-2,1,1,-1,-1]
dx = [1,-1,1,-1,2,-2,2,-2]

cx = 0
cy = 0

for i in range(8):
    if horizon[i]==place[0]:
        cx = i+1
        break
cy = int(place[1])

count = 0
for i in range(8):
    ny=cy+dy[i]
    nx=cx+dx[i]
    if 0 < ny < 9 and 0 < nx < 9:
        count += 1
