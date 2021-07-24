N = int(input())
again = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(1, 11):
        if row[j-1] != (((j-1) % 5) +1):
            break
    else:
        again.append(i+1)
for num in again:
    print(num)