# https://www.acmicpc.net/problem/4673
# 셀프넘버

isSelf = [True]*10001

for num in range(10000):
    total = num + sum(map(int, list(str(num))))

    if total <=10000:
        isSelf[total]=False

for i in range(1,10000):
    if isSelf[i]:
        print(i)