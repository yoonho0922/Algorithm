import sys
readline = sys.stdin.readline

def verify(cur, next):

    for j in range(len(cur)):
        if cur[j] != next[j]:
            return True # 일관성 있음

    return False # 일관성 없음

T = int(readline())

for _ in range(T):
    N = int(readline())
    numbers = []

    for _ in range(N):
        numbers.append(readline().strip())

    numbers.sort()
    result = 'YES'

    for i in range(N-1):
        if not verify(numbers[i], numbers[i+1]):
            result = 'NO'

    print(result)