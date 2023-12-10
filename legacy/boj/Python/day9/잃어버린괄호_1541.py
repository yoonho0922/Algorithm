arr = list(input().split('-'))

s = 0
for num in arr[0].split('+'):
    s += int(num)

minimum = s

for i in range(1, len(arr)):
    s = 0
    for num in arr[i].split('+'):
       s += int(num)
    minimum -= s

print(minimum)