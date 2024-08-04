# https://www.acmicpc.net/problem/14890

# 1. 한 줄에 대해 검사. 양 방향으로 검사. 경사로를 놓은 여부.
# 2. 2 이상 차이나는 블록이 존재하면 불가
# 3. 1 차이나는 블록이 있다면 연석된 길이와 경사로 여부 체크
# 4. 경사로 여부는 한 줄에 대해 독립 시행이다. (예제4)

def check_single_way(arr, installed):
    for i in range(1, N):
        # 높이가 2 이상 차이나면 지나갈 수 없다
        if arr[i] - arr[i-1] > 1:
            return False
        # 높이가 차이가 1이라면 경사로를 둘 수 있는지 확인한다
        elif arr[i] - arr[i-1] == 1:
            if i-L >= 0:
                for j in range(i-L, i):
                    if arr[j] == arr[i-1] and not installed[j]:
                        installed[j] = True
                    else:
                        return False
            else:
                return False
    return True

def check_road(road):
    installed = [False] * N
    # 왼쪽에서 오른쪽으로 높아지는 부분 확인
    right_passable = check_single_way(road, installed)
    # 오른쪽에서 왼쪽으로 높아지는 부분 확인
    left_passable = check_single_way(road[::-1], installed[::-1])

    return right_passable and left_passable


# main
N, L = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for row in G:
    if check_road(row):
        ans += 1

for col in zip(*G):
    if check_road(list(col)):
        ans += 1

print(ans)