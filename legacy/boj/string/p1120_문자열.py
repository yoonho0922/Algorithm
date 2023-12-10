A, B = input().split()
N, M = len(A), len(B)

ans=99999999999

for i in range(M-N+1):
    cnt = 0
    for j in range(N):
        if A[j] != B[i+j]:
            cnt+=1
    ans = min(ans, cnt)

print(ans)
