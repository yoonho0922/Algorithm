import math
A, B, C = map(int, input().split())
if C>B:
    if A%(C-B)==0:
        print(A//(C-B)+1)
    else:
        print(math.ceil(A/(C-B)))
else:
    print(-1)