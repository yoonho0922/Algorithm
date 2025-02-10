# https://www.acmicpc.net/problem/2304

N = int(input())
tops = [list(map(int, input().split())) for _ in range(N)]

tops.sort(key=lambda x: x[0])

# 제일 높은 탑의 높이와 index 구하기
max_index, max_height = 0, 0
for i in range(N):
    if tops[i][1] > max_height:
        max_index = i
        max_height = tops[i][1]

# 넓이 계산
answer = max_height

# 왼쪽 좌표에서 높은 기둥 좌표 전까지
cur_height = tops[0][1]
for i in range(1, max_index + 1):
    width = tops[i][0] - tops[i-1][0]
    answer += width * cur_height
    cur_height = max(cur_height, tops[i][1])
# # 오른쪽에서 높은 기둥 까지
cur_height = tops[N-1][1]
for i in range(N-2, max_index-1, -1):
    width = tops[i+1][0] - tops[i][0]
    answer += width * cur_height
    cur_height = max(cur_height, tops[i][1])
print(answer)