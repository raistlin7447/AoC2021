import statistics

with open("day7_input.txt") as f:
    crabs = list(map(int, f.readline().strip().split(",")))
    mid = int(statistics.median(crabs))
    fuel = sum([abs(crab - mid) for crab in crabs])
    print(f"{fuel=}")
