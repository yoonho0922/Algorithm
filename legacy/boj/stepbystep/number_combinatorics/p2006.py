N, K = map(int, input().split())

def count_two(num):
    cnt = 0
    while num != 0:
        cnt += num//2
        num = num//2
    return cnt

def count_five(num):
    cnt = 0
    while num != 0:
        cnt += num//5
        num = num//5
    return cnt

print(min(count_two(N)-count_two(K)-count_two(N-K),
          count_five(N)-count_five(K)-count_five(N-K)))