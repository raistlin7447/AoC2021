with open("day5_input.txt") as f:
    lines = f.readlines()
    grid = [[0 for i in range(1000)] for j in range(1000)]
    for line in lines:
        start, end = map(str.strip, line.split(" -> "))
        start_x, start_y = map(int, start.split(","))
        end_x, end_y = map(int, end.split(","))

        # Diagonal
        if start_x != end_x and start_y != end_y:
            if start_x > end_x:
                start_x, start_y, end_x, end_y = end_x, end_y, start_x, start_y
            slope = (end_y - start_y) // (end_x - start_x)
            for y, x in zip(range(start_x, end_x+1), range(start_y, end_y+slope, slope)):
                grid[x][y] += 1

        # Horizontal and Vertical
        else:
            x_step = 1 if end_x >= start_x else -1
            y_step = 1 if end_y >= start_y else -1
            for y in range(start_x, end_x+x_step, x_step):
                for x in range(start_y, end_y+y_step, y_step):
                    grid[x][y] += 1

    total = sum([1 for x in grid for y in x if y > 1])
    print(f"{total=}")
