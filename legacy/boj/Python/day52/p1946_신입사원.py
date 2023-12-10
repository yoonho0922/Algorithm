import sys
readline = sys.stdin.readline

T = int(readline())
for _ in range(T):
    N = int(readline())
    arr = []
    for _ in range(N):
        li = list(map(int, readline().strip().split()))
        arr.append(li)
    arr.sort()

    ans, head = 1, arr[0][1]
    for i in range(1, N):
        if arr[i][1] < head:
            ans += 1
            head = arr[i][1]

    print(ans)