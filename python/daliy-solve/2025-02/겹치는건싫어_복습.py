# https://www.acmicpc.net/problem/20922

N, K = map(int, input().split())
nums = list(map(int, input().split()))
bucket = [0] * (100_000 + 1)
s, e, answer = 0, -1, 0

while e < N - 1:
    while e < N - 1 and bucket[nums[e + 1]] < K:
        bucket[nums[e + 1]] += 1
        e += 1
        answer = max(answer, e - s + 1)
    bucket[nums[s]] -= 1
    s += 1

print(answer)

s =set()
s.add([])