N = int(input())
P = list(map(int, input().split()))
P.sort()
ans = 0
for i in range(N):
    ans += sum(P[:i+1])
print(ans)