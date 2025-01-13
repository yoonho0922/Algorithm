# https://www.acmicpc.net/problem/1092

N = int(input())
ships = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

boxes.sort(reverse=True)
works = [0] * N

for box in boxes:
    # 처리 가능한 배 중 가장 적게 작업한 배를 선택
    availables = [i for i in range(N) if ships[i] >= box]
    if availables:
        # 최소 작업량을 가진 배 선택
        selected = min(availables, key=lambda i: works[i])
        works[selected] += 1
    else:
        # 처리 가능한 배가 없으면 종료
        print(-1)
        exit()

# 최대 작업량 출력
print(max(works))
