y, x = {}, {}
for _ in range(3):
    b, a = map(int, input().split())

    if y.get(b):
        y[b]+=1
    else:
        y[b]=1

    if x.get(a):
        x[a]+=1
    else:
        x[a]=1
ans = [0,0]
for b in y:
    if y[b]==1:
        ans[0]=b
        break
for a in x:
    if x[a]==1:
        ans[1]=a
        break
print(*ans)
