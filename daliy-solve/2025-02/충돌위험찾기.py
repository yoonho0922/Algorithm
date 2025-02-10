def get_paths(points, route):
    paths = [(points[route[0] - 1][0], points[route[0] - 1][1])]
    for i in range(len(route) - 1):
        cur_y, cur_x = points[route[i] - 1]
        target_y, target_x = points[route[i + 1] - 1]
        while cur_y != target_y:
            cur_y = cur_y + 1 if cur_y < target_y else cur_y - 1
            paths.append((cur_y, cur_x))
        while cur_x != target_x:
            cur_x = cur_x + 1 if cur_x < target_x else cur_x - 1
            paths.append((cur_y, cur_x))
    return paths



def solution(points, routes):
    all_paths = [get_paths(points, route) for route in routes]
    max_length = max([len(paths) for paths in all_paths])
    for p in all_paths:
        print(p)
    answer = 0
    for i in range(max_length):
        robots = set()
        conflicts = []
        for paths in all_paths:
            if len(paths) > i:
                if paths[i] in robots:
                    conflicts.append(paths[i])
                else:
                    robots.add(paths[i])
        answer += len(conflicts)
    return 0

solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [2, 4]])