N = int(input())
P = list(map(int, input().split()))

dt = [1]*N
db = [1]*N

for i in range(N):
    for j in range(i):
        if P[j] < P[i]:
            dt[i] = max(dt[i], dt[j]+1)

for i in range(N):
    for j in range(i):
        if P[j] > P[i]:
            db[i] = max([db[i], dt[j]+1, db[j]+1])

# print(dt)
# print(db)
print(max(db))
