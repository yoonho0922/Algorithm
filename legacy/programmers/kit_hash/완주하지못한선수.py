def solution(participant, completion):
    answer = ''
    d = dict()
    for c in completion:
        if d.get(c):
            d[c] += 1
        else:
            d[c] = 1
    for p in participant:
        if d.get(p) and d[p] > 0:
            d[p] -= 1
        else:
            answer = p
            break

    return answer

solution()