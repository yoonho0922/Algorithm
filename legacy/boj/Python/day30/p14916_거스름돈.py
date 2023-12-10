N = int(input())
ans = 0
for i in range(5):
    if N%5 == 0:
        print(ans + N//5)
        break
    elif N == 0:
        print(ans)
        break
    elif N < 0:
        print(-1)
        break

    N -= 2
    ans += 1

