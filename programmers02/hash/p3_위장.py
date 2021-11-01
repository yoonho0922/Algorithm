def solution(clothes):
    d = dict()

    for c, ctype in clothes:
        if d.get(ctype):
            d[ctype] += 1
        else:
            d[ctype] = 1

    answer = 1

    for num in d.values():
        answer *= (num + 1)

    return answer - 1