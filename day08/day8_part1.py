with open("day8_input.txt") as f:
    lines = map(str.strip, f.readlines())
    count = 0
    for signals, outputs in [(x.split(), y.split()) for x, y in [line.split("|") for line in lines]]:
        count += sum(1 for output in outputs if len(output) in [2, 4, 3, 7])
    print(f"{count=}")
