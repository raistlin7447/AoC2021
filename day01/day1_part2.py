with open("day1_input.txt") as f:
    depths = list(map(int, f.readlines()))
    previous = sum(depths[:3])
    total = 0
    num_items = len(depths)
    for i in range(1, num_items+1):
        if i+3 > num_items:
            break
        current = sum(depths[i:i+3])
        if current > previous:
            total += 1
        previous = current
    print(f"{total=}")
