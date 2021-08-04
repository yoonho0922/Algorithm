W = input()
n = len(W)

def sol():
    for x in range(1, n+1):
        s, e = 0, x-1
        A = W[s:e+1]
        while True:
            cur = B = int(W[s:e+1])

            if e == n-1:
                return [int(A), int(B)]

            s = e+1
            e = s + len(str(cur+1))-1

            if e<n and cur+1 == int(W[s:e+1]):
                continue
            else:
                break


print(*sol())