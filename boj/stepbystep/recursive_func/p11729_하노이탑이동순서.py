def sol(num, start, target, through):
    if num==1:
        print(start, target)
        return
    sol(num-1, start, through, target)
    print(start, target)
    sol(num-1, through, target, start)

N = int(input())
print(2**N-1)
sol(N, 1, 3, 2)