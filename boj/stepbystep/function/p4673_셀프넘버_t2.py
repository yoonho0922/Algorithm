self_number=[True]*10001
for i in range(1,10001):
    for j in str(i):
        i += int(j)
    if i <10001:
        self_number[i]=False

for i in range(1, 10001):
    print("{}\n".format(i) if self_number[i] else '',end='')