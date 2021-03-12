exp = list(input().split('-'))
cur = list(map(int, exp[0].split('+')))
ans = sum(cur)
for i in range(1, len(exp)):
    cur = list(map(int, exp[i].split('+')))
    ans -= sum(cur)
print(ans)