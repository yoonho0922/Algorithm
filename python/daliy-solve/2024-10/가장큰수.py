# https://school.programmers.co.kr/learn/courses/30/lessons/42746

MAX_SIZE = 4 # 원소의 최대 길이

# int array를 (원래 문자열, 4자리 문자열) array로 변환한다.
def expand(number):
    s = str(number)
    expanded = s
    # 4 자리가 아닌 수는 앞의 수를 반복하여 4 자리를 맞춘다.
    # ex) 1 -> 1111, 13 -> 1313, 132 -> 1321
    for i in range(MAX_SIZE - len(s)):
        expanded += s[i % len(s)]
    return int(expanded)


def solution(numbers):
    answer = ""
    numbers.sort(reverse = True, key=lambda x : expand(x))
    for num in numbers:
        answer += str(num)

    return str(int(answer))