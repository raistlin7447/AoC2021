import statistics

# Brute Force
with open("day7_input.txt") as f:
    crabs = list(map(int, f.readline().strip().split(",")))
    best = 2**10000
    fuel = lambda distance: int(distance * (distance+1) / 2)
    for i in range(min(crabs), max(crabs)+1):
        total_fuel = sum(fuel(abs(crab - i)) for crab in crabs)
        best = min(best, total_fuel)
    print(f"{best=}")

# Turns out that mean is usually correct, but can sometimes vary by up to 1/2
# https://www.reddit.com/gallery/rawxad
with open("day7_input.txt") as f:
    crabs = list(map(int, f.readline().strip().split(",")))
    fuel = lambda distance: int(distance * (distance+1) / 2)
    total_fuel = lambda x: sum(fuel(abs(crab - x)) for crab in crabs)
    mean = statistics.mean(crabs)
    low = int(mean - 0.5)
    high = int(mean + 0.5)
    best = min(total_fuel(low), total_fuel(high))
    print(f"{best=}")
