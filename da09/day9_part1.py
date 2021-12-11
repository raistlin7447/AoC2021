with open("day9_input.txt") as f:
    lines = list(map(str.strip, f.readlines()))
    grid = [[int(col) for col in row] for row in lines]
    local_mins = []

    for row_i, row in enumerate(grid):
        for col_i, val in enumerate(row):
            neighbors = []
            for row_shift, col_shift in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                try_row = row_i + row_shift
                try_col = col_i + col_shift
                if try_row < 0 or try_col < 0 or try_row > len(grid)-1 or try_col > len(row)-1:
                    continue
                neighbors.append(grid[try_row][try_col])

            if all(val < x for x in neighbors):
                local_mins.append(val)

    total = sum(local_mins) + len(local_mins)
    print(f"{total=}")
