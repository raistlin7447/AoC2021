with open("day7_input.txt") as f:
    crabs = list(map(int, f.readline().strip().split(",")))
    best = 2**10000
    fuel = lambda distance: int(distance * (distance+1) / 2)
    for i in range(min(crabs), max(crabs)+1):
        total_fuel = sum(fuel(abs(crab - i)) for crab in crabs)
        best = min(best, total_fuel)
    print(f"{best=}")
