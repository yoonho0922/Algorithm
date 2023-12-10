A, B = input().split()
X, Y = '', ''
for i in range(3):
    X += A[2-i]
    Y += B[2-i]
print(X if int(X)>int(Y) else Y)