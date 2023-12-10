import math

N = str(input())

bucket = [0] * 10
for i in range(len(N)):
    if int(N[i]) == 9:
        bucket[6] += 1
    else:
        bucket[int(N[i])] += 1

bucket[6] = math.ceil(bucket[6]/2)
print(max(bucket))