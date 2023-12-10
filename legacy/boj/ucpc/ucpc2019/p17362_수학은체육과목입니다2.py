N = int(input())
ans = N%8
if ans == 6:
    print(4)
elif ans == 7:
    print(3)
elif ans == 0:
    print(2)
else:
    print(ans)