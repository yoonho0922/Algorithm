# https://www.acmicpc.net/problem/21758

def sublist(N, honeys):
    sub_honeys = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        sub_honeys[i] = sub_honeys[i + 1] + honeys[i]
    return sub_honeys


# 벌1을 왼쪽 끝에, 꿀통을 오른쪽 끝에 놓는 케이스
def max_side_bucket(N, honeys):
    sub_honeys = sublist(N, honeys)
    # print("info", sub_honeys)

    result = 0

    for i in range(N - 2, 0, -1):
        # 벌1의 수확 + 벌2의 수확
        here = (sub_honeys[1] - honeys[i]) + sub_honeys[i + 1]
        # print("info", i, here)
        result = max(result, here)

    return result


# 벌1, 벌2를 양 끝에 두고 사이에 꿀통을 넣는 케이스
def max_middle_bucket(N, honeys):
    sub_honeys = sublist(N, honeys)
    # print("info sub", sub_honeys)
    result = 0
    for i in range(1, N - 1):
        left = sub_honeys[1] - sub_honeys[i+1]
        right = sub_honeys[i] - honeys[N-1]
        # print("info", i, left, right)
        result = max(result, left + right)
    return result


N = int(input())
honeys = list(map(int, input().split()))

# print(max_side_bucket(N, honeys))
# print(max_side_bucket(N, honeys[::-1]))
# print(max_middle_bucket(N, honeys))
answer = max([max_side_bucket(N, honeys), max_side_bucket(N, honeys[::-1]), max_middle_bucket(N, honeys)])
print(answer)