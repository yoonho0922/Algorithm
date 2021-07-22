N=cur = int(input())
cnt = 0
while cnt==0 or cur!=N:
    if cur<10: cur = cur*10 + cur
    else: cur = cur%10*10 + (cur//10 + cur%10)%10
    cnt+=1
print(cnt)