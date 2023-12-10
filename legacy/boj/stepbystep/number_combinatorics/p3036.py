N = int(input())
P = list(map(int, input().split()))

def sol(a, b):
    # get com factor
    cf = 1
    for i in range(2, b+1):
        if a%i==0 and b%i==0:
            cf = i
    return "{}/{}".format(a//cf, b//cf)


for i in range(N-1):
    print(sol(P[0], P[i+1]))