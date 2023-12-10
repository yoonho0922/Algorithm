def check(x):
    cnt = 0
    # 빌딩의 왼족 확인
    for i in range(x):
        weight = x - i
        height = abs(p[i] - p[x])
        # 걸치는 빌딩이 있는지 확인
        for j in range(i+1, x):
            if p[i] >= p[x]:
                roof = p[x] - height * (j - x) / weight
            else:
                roof = p[x] + height * (j - x) / weight
            # 걸치는 빌딩이 있으면 count 안 함
            if p[j] >= roof:
                break
        else:
            cnt += 1


    # 빌딩의 오른쪽 확인
    for i in range(x+1, N):
        weight = i - x
        height = abs(p[i] - p[x])
        # 걸치는 빌딩이 있는지 확인
        for j in range(x + 1, i):
            if p[i] >= p[x]:
                roof = p[x] + height * (j - x) / weight
            else:
                roof = p[x] - height * (j - x) / weight
            # 걸치는 빌딩이 있으면 count 안 함
            if p[j] >= roof:
                break
        else:
            cnt += 1

    return cnt



N = int(input())
p = list(map(int, input().split()))

result = []

for i in range(N):
    cnt = check(i)
    result.append(cnt)

print(max(result))