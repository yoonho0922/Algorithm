alpha=[2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
S = input()
ans = 0
for s in S:
    ans += alpha[ord(s)-65]+1
print(ans)