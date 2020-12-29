import sys

def find_square(s):
    # 정사각형의 꼭지점의 숫자 크기가 같은 경우를 찾음
    for i in range(N-s+1):
        for j in range(M-s+1):
            if numbers[i][j] == numbers[i][j+s-1] \
                    == numbers[i+s-1][j] == numbers[i+s-1][j+s-1]:
                return True

    return False


N, M = map(int, input().split())
numbers = []

for i in range(N):
    li = list(map(int, input()))
    numbers.append(li)

size = min(N, M)

# 최대 크기부터 하나씩 줄여가며 시작
for s in range(size, 0, -1):
    if find_square(s):
        print(s**2)
        break


