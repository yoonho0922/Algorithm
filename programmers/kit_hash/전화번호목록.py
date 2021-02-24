def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for i in range(len(phone_number) -1 ):
            temp += phone_number[i]
            if hash_map.get(temp):
                answer = False

    return answer

solution(["119", "97674223", "1195524421"])