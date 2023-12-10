N = int(input())
ans = 0
for i in range(1, N+1):
    if i<100:
       ans += 1
    elif i>=100 and i<1000:
        a, b, c = str(i)[0], str(i)[1], str(i)[2]
        if 2*int(b) == (int(a) + int(c)):
            ans += 1
print(ans)