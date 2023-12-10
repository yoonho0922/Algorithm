S=input()
ans = 0
for i in range(len(S)):
    if S[i]==' ' and i != 0 and i != len(S)-1:
        ans += 1
print(ans+1 if S!=' ' else 0)