N = int(input())

def sol(depth):
    if depth==0:
        return 0
    elif depth==1:
        return 1
    return sol(depth-1) + sol(depth-2)


print(sol(N))