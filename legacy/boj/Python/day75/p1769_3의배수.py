def sol(num, depth):
    if len(num) <=1:
        print(depth)
        print("YES" if int(num)%3==0 else "NO")
        exit()

    conv = 0
    for i in num:
        conv += int(i)
    sol(str(conv), depth+1)

X = input()
sol(X, 0)