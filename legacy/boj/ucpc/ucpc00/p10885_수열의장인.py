def sol(N, nums):

    d = [0]*(N+1)

    for i in range(N):
        if nums[i]==0:
            d[i+1] = 0
        elif nums[i]<0:
            d[i+1] = d[i]+1
        elif nums[i]>0:
            d[i+1] = d[i]

    


T = int(input())
for _ in range(T):
    N = int(input())
    S = list(map(int, input().split()))

    print(sol(N, S))

    # # 0 앞뒤로 스플릿
    # splited = []
    # pre=0
    #
    # # for i in range(N):
    # #     if S[i]==0 and pre<i:
    # #         splited.append(S[pre:i])
    # #         pre=i+1
    # # if pre<N+1:
    # #     splited.append(S[pre:N+1])
    # # print(splited)
    # #
    # # ans = -99999999
    # # # for nums in splited:
    # # #     ans = max(ans, sol(nums))