S = input()
x = 1
while x <=len(S):
    if S[x:x+x] == str(int(S[:x]) + 1): # 그 다음 숫자의 자릿수가 같을 때
        break
    if S[x:x+x+1] == str(int(S[:x]) + 1): # 그 다음 숫자의 자릿수가 올라갓을 때
        break
    x += 1

A = B = int(S[:x])

while True:
    if int(S[len(S)-x:]) >= A:
        B = int(S[len(S)-x:])
        break
    x += 1


print(A, B)