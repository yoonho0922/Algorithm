N = int(input())
times = list(map(int, input().split()))
ans, preWating = 0, 0
times.sort()
for time in times:
    ans += time + preWating
    preWating += time
print(ans)