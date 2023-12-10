def solution(answers):
    answer = []
    pattern = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    score = [0, 0, 0]

    for i in range(len(answers)):
        for j in range(3):
            idx = i % len(pattern[j])
            if answers[i] == pattern[j][idx]:
                score[j] += 1

    for i, s in enumerate(score):
        if s == max(score):
            answer.append(i + 1)

    return answer