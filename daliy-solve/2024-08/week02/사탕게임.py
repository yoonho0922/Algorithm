# https://www.acmicpc.net/problem/3085

def switch_row_and_get_longest(grid):
    longest = 0

    for y in range(N-1):
        for x in range(N):
            if grid[y][x] == grid[y + 1][x]:
                continue
            grid[y][x], grid[y + 1][x] = grid[y + 1][x], grid[y][x]
            longest = max(longest, get_longest_col(grid))
            grid[y][x], grid[y + 1][x] = grid[y + 1][x], grid[y][x]

    return longest

def get_continuous_col(row, grid):
    longest, cnt = 0, 1
    prev = grid[row][0]

    for x in range(1, N):
        if prev == grid[row][x]:
            cnt += 1
            longest = max(longest, cnt)
        else:
            cnt = 1
        prev = grid[row][x]

    return cnt


def get_longest_col(grid):
    longest = 0

    for y in range(N):
        continuous = get_continuous_col(y, grid)
        longest = max(longest, continuous)

    rotated = [list(r) for r in list(zip(*grid))]

    for y in range(N):
        continuous = get_continuous_col(y, rotated)
        longest = max(longest, continuous)

    return longest

N = int(input())
G = [list(input()) for _ in range(N)]
rotated = [list(r) for r in list(zip(*G))]

ans = switch_row_and_get_longest(G)
ans = max(ans, switch_row_and_get_longest(rotated))

print(ans)