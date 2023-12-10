N = int(input())
heights = list(map(int, input().split()))
count = sum(heights)//3 # 총 물을 주는 횟수
x = 0  # 2로 나눌 수 있는 갯수

for h in heights:
    x += h // 2

print("YES" if sum(heights)%3 == 0 and x>=count else "NO")