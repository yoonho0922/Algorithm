def dfs(s, d): # start, depth
    # 끝에 도달하면
    if d == 6:
        for i in range(6):
            print(C[i], end=' ')
        print()

    for i in range(s, len(nums)):
        C[d] = nums[i]
        dfs(i+1, d+1)

C = [0]*12


while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    del nums[0] # 첫번째 수 k 삭제
    dfs(0, 0)
    print()