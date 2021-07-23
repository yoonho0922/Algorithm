nums=set()
for _ in range(10):
    x = int(input())
    nums.add(x%42)
print(len(nums))