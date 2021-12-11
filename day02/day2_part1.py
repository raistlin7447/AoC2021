with open("day2_input.txt") as f:
    instructions = f.readlines()
    horizontal_pos = 0
    depth_pos = 0
    for instruction in instructions:
        match instruction.split():
            case ["forward", units]:
                horizontal_pos += int(units)
            case ["down", units]:
                depth_pos += int(units)
            case ["up", units]:
                depth_pos -= int(units)

    result = horizontal_pos * depth_pos
    print(f"{result=}")
