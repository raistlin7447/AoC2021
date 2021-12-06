with open("day3_input.txt") as f:
    numbers = f.readlines()
    bit_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    total_numbers = len(numbers)
    for number in numbers:
        for i, value in enumerate(number.strip()):
            bit_counts[i] += int(value)
    gamma_rate = ""
    epsilon_rate = ""
    for bit_count in bit_counts:
        if bit_count > total_numbers / 2:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    gamma_int = int(gamma_rate, 2)
    epsilon_int = int(epsilon_rate, 2)
    result = gamma_int * epsilon_int
    print(f"{result=}")
