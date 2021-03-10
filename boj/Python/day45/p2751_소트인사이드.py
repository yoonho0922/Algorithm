arr = list(map(int, input()))
arr.sort(reverse=True)
for a in arr:
    print(a, end="")