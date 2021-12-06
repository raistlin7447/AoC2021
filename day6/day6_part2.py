with open("day6_input.txt") as f:
    initial_fish = list(map(int, f.readline().strip().split(",")))
    fish = [0] * 9
    for initial_f in initial_fish:
        fish[initial_f] += 1
    for day in range(256):
        new_fish = [0] * 9
        for state in range(9):
            if state == 0:
                new_fish[6] += fish[0]
                new_fish[8] += fish[0]
            else:
                new_fish[state-1] += fish[state]
        fish = new_fish
    print(sum(fish))
