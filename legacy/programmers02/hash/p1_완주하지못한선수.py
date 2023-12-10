def solution(part, comp):
    d = dict()

    for c in comp:
        if d.get(c):
            d[c] += 1
        else:
            d[c] = 1

    for p in part:
        if d.get(p) and d[p] >= 1:
            d[p] -= 1
        else:
            return p