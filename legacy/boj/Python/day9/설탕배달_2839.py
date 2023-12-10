N = int(input())

total = 0

while True:

    if N % 5 == 0:
        total += N // 5
        print(total)
        break

    N -= 3
    total += 1

    if N < 0:
        print(-1)
        break