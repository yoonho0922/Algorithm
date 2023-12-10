# N = int(input())
# for i in range(1,10):
#     print("{} * {} = {}".format(N, i, N*i))
'''p8393'''

# N = int(input())
# ans=0
# for i in range(1, N+1):
#     ans+=i
# print(ans)

'''p15552'''
# import sys
# readline = sys.stdin.readline
# T = int(input())
# for _ in range(T):
#     a, b = map(int, readline().split())
#     print(a+b)

'''p2741'''
# N = int(input())
# for i in range(1, N+1):
#     print(i)

'''p2742'''
# N = int(input())
# for i in range(N, 0, -1):
#     print(i)

'''p11021'''
# import sys
# readline = sys.stdin.readline
# T = int(input())
# for i in range(T):
#     a, b = map(int, readline().split())
#     print("Case #{}: {}".format(i+1, a+b))

'''p11022'''
# import sys
# readline = sys.stdin.readline
# T = int(input())
# for i in range(T):
#     a, b = map(int, readline().split())
#     print("Case #{}: {} + {} = {}".format(i+1, a, b, a+b))

'''p10871'''
N, X = map(int, input().split())
nums = list(map(int, input().split()))
for num in nums:
    print(str(num)+' ' if num<X else '', end='')