N = int(input())

def sol(x):
    if x==0 or x==1:
        return 
    return x*sol(x-1)

print(sol(N))