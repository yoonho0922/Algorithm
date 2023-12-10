def dfs(d): #depth

    if d == 3:
        for i in range(3):
            print(C[i], end=' ')
        print()
        return

    for i in range(len(arr)):
        if select[i]: continue
        select[i] = True
        C[d] = arr[i]
        dfs(d + 1)
        select[i] = False

C = [0]*3
arr = list(map(int, '12345'))
select = [False]*len(arr)
dfs(0)