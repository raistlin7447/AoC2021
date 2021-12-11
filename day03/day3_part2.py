with open("day3_input.txt") as f:
    numbers = list(map(str.strip, f.readlines()))
    num_bits = len(numbers[0])

    candidates = numbers
    for i in range(num_bits):
        zeros = []
        ones = []
        for candidate in candidates:
            if candidate[i] == "0":
                zeros.append(candidate)
            else:
                ones.append(candidate)

        if len(zeros) <= len(ones):
            if len(ones) == 1:
                oxygen_rating = ones[0]
                break
            else:
                candidates = ones
        else:
            if len(zeros) == 1:
                oxygen_rating = zeros[0]
                break
            else:
                candidates = zeros

    candidates = numbers
    for i in range(num_bits):
        zeros = []
        ones = []
        for candidate in candidates:
            if candidate[i] == "0":
                zeros.append(candidate)
            else:
                ones.append(candidate)

        if len(zeros) <= len(ones):
            if len(zeros) == 1:
                co2_rating = zeros[0]
                break
            else:
                candidates = zeros
        else:
            if len(ones) == 1:
                co2_rating = ones[0]
                break
            else:
                candidates = ones

    oxygen_int = int(oxygen_rating, 2)
    co2_int = int(co2_rating, 2)
    result = oxygen_int * co2_int
    print(f"{result=}")
