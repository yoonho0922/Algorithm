# https://www.acmicpc.net/problem/5397

def get_pw(logs):
    fs, bs = [], []

    for key in logs:
        if key == '-':
            if fs:
                fs.pop()
        elif key == '<':
            if fs:
                bs.append(fs.pop())
        elif key == '>':
            if bs:
                fs.append(bs.pop())
        else:
            fs.append(key)

    return fs + bs[::-1]

T = int(input())
for _ in range(T):
    logs = input()
    print(''.join(get_pw(logs)))
