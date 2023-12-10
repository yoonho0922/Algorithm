S = input()
x = 1
while x <=len(S):
    if S[x:x+x] == str(int(S[:x]) + 1): # 그 다음 숫자의 자릿수가 같을 때
        break
    if S[x:x+x+1] == str(int(S[:x]) + 1): # 그 다음 숫자의 자릿수가 올라갓을 때
        break
    x += 1

A = B = int(S[:x])

i = 0

while i < len(S):
    x = len(str(B))
    print(x)
    if S[i:i+x] == str(B):
        i = i+x
        B += 1

print(A, B-1)