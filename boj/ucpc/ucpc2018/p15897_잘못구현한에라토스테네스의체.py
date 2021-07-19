N = int(input())

ans, i = 0, 1

while i<N:
    x = N//i if N%i==0 else int(N/i)+1
    print(i, x, ans)
    ans += x * (int((N - 1) / (x - 1)) + 1 - i)
    i = int((N - 1) / (x - 1)) + 1

print(ans+1)