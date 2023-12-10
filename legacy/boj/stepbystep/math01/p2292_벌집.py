x = int(input())
i = int(((x-1)/3)**0.5) + 1
while True:
    if (x-1)/3 <= i*(i-1):
        print(i)
        break
    i += 1

