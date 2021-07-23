T=int(input())
for _ in range(T):
    row = list(map(int, input().split()))
    avg = sum(row[1:])/row[0]
    cnt = 0
    for num in row[1:]:
        if num>avg:
            cnt+=1
    print(f"{cnt/row[0]*100:.3f}%")