def print_grid(grid, with_space=False):
    for r in grid:
        for c in r:
            if not with_space:
                print(c, end="")
            else:
                print(f"{c:3}", end="")
        print("\n", end="")
    print("\n", end="")


def increment_grid(grid):
    return [[col + 1 for col in row] for row in grid]


def increment_adjacent(grid, location):
    row, col = location
    for row_i in [-1, 0, 1]:
        for col_i in [-1, 0, 1]:
            if (row_i, col_i) != (0, 0):
                try_row = row + row_i
                try_col = col + col_i
                if 0<= try_row <= 9 and 0 <= try_col <= 9:
                    grid[try_row][try_col] += 1
    return grid


def flash_grid(grid, flashed=None):
    if flashed is None:
        flashed = set()
    for row in range(10):
        for col in range(10):
            if grid[row][col] > 9 and (row, col) not in flashed:
                flashed.add((row, col))
                grid = increment_adjacent(grid, (row, col))
                grid, flashed = flash_grid(grid, flashed)
    return grid, flashed


def reset_flashed(grid, flashed):
    for row, col in flashed:
        grid[row][col] = 0
    return grid


with open("day11_input.txt") as f:
    lines = list(map(str.strip, f.readlines()))
    grid = [[int(col) for col in row] for row in lines]

    total_flashed = 0
    for step in range(100):
        grid = increment_grid(grid)
        grid, flashed = flash_grid(grid)
        total_flashed += len(flashed)
        grid = reset_flashed(grid, flashed)

    print(f"{total_flashed=}")
