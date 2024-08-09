# https://www.acmicpc.net/problem/3085


def check_longest(grid):
    longest = 1
    for i in range(N):
        length = 1
        prev = grid[i][0]
        for j in range(1, N):
            if prev == grid[i][j]:
                length += 1
                longest = max(longest, length)
            else:
                length = 1
            prev = grid[i][j]
    return longest

def solve_row(grid):
    longest = 0
    for i in range(N-1):
        for j in range(N):
            if grid[i][j] != grid[i+1][j]:
                grid[i][j], grid[i+1][j] = grid[i+1][j], grid[i][j]
                longest = max(longest, check_longest(grid))
                rotated = [list(r) for r in list(zip(*grid))]
                longest = max(longest, check_longest(rotated))
                grid[i][j], grid[i+1][j] = grid[i+1][j], grid[i][j]
    return longest

# main
N = int(input())
G = [list(input()) for _ in range(N)]
rotated_G = [list(r) for r in list(zip(*G))]


ans = solve_row(G)
ans = max(ans, solve_row(rotated_G))

print(ans)