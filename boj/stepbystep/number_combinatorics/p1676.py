N = int(input())
ans = 0
for i in range(2, N+1):
    while i%5==0:
        ans += 1
        i = i//5

print(ans)