UCPC = ['U','C','P','C']
words = input()
x=0
for c in words:
    if c == UCPC[x]:
        x+=1
    if x>3:
        break
print("I love UCPC" if x==4 else "I hate UCPC")