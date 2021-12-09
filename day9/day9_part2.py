with open("day9_input.txt") as f:
    lines = list(map(str.strip, f.readlines()))
    grid = [[int(col) for col in row] for row in lines]

    basins = []
    done = set()
    for row_i, row in enumerate(grid):
        for col_i, val in enumerate(row):
            current_location = (row_i, col_i)
            if current_location not in done and val != 9:
                basin = []
                neighbors = [current_location]
                while neighbors:
                    popped = neighbors.pop()
                    if popped in done:
                        continue
                    done.add(popped)
                    basin.append(popped)
                    for row_shift, col_shift in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        try_row = popped[0] + row_shift
                        try_col = popped[1] + col_shift
                        if try_row < 0 or try_col < 0 or try_row > len(grid)-1 or try_col > len(row)-1 or grid[try_row][try_col] == 9:
                            continue
                        neighbors.append((try_row, try_col))
                basins.append(basin)

    basins.sort(key=lambda x: len(x), reverse=True)
    total = len(basins[0]) * len(basins[1]) * len(basins[2])
    print(f"{total=}")
