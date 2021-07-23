import sys
readline = sys.stdin.readline

T = int(input())
for _ in range(T):
    case = readline().strip()
    i, score = 1, 0
    for c in case:
        if c=='O':
            score += i
            i+=1
        else:
            i=1
    print(score)