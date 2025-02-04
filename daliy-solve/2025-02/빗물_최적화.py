H, W = map(int, input().split())
blocks = list(map(int, input().split()))
left_max = [0] * W
right_max = [0] * W
left_max[0] = blocks[0]
for i in range(1, W):
    left_max[i] = max(left_max[i - 1], blocks[i])
right_max[W - 1] = blocks[W - 1]
for i in range(W-2, -1, -1):
    right_max[i] = max(right_max[i + 1], blocks[i])
answer = 0
for i in range(W):
    answer += min(left_max[i], right_max[i]) - blocks[i]
print(answer)