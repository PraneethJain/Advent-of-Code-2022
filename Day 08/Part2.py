with open("./Day 8/input.txt") as f:
    grid = [list(map(int, line.strip())) for line in f.readlines()]
    length = len(grid)

    def get_scene_score(i, j):
        scene_score = 1
        for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            direction_score = 0
            cur_x, cur_y = i + x, j + y

            while 0 <= cur_x < length and 0 <= cur_y < length:
                direction_score += 1
                if grid[cur_x][cur_y] >= grid[i][j]:
                    break

                cur_x += x
                cur_y += y

            scene_score *= direction_score

        return scene_score

    print(max(get_scene_score(i, j) for i in range(length) for j in range(length)))
