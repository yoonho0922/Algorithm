def multipleOf3():
    # 1. 0이 1개 이상인지 검사
    for num in S:
        if num==0:
            break
    else:
        return False

    # 2. 각 자리 숫자 합이 3의 배수인지 검사
    if sum(S) % 3 != 0:
        return False

    return True

S = list(map(int, input()))


if multipleOf3():
    S.sort(reverse=True)
    print(''.join(list(map(str, S))))
else:
    print(-1)