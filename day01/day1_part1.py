with open("day1_input.txt") as f:
    depths = list(map(int, f.readlines()))
    previous = depths[0]
    total = 0
    for depth in depths[1:]:
        if depth > previous:
            total += 1
        previous = depth
    print(f"{total=}")
