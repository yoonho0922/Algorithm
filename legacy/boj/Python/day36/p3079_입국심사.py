import sys
readline = sys.stdin.readline

def search(left, right, target):
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        pass_people = 0

        for t in T:
            pass_people += mid//t

        if pass_people >= target:
            answer = mid
            right = mid-1
        elif pass_people < target:
            left = mid+1

    return answer

N, M = map(int, readline().split())
T = []
for _ in range(N):
    T.append(int(readline()))
T.sort()

print(search(T[0], T[-1] * M, M))