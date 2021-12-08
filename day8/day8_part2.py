from collections import Counter, defaultdict

with open("day8_input.txt") as f:
    lines = map(str.strip, f.readlines())

    seven_segment_map = {
        "abcefg":   "0",
        "cf":       "1",
        "acdeg":    "2",
        "acdfg":    "3",
        "bcdf":     "4",
        "abdfg":    "5",
        "abdefg":   "6",
        "acf":      "7",
        "abcdefg":  "8",
        "abcdfg":   "9",
    }

    total = 0
    for signals, outputs in [(x.split(), y.split()) for x, y in [line.split("|") for line in lines]]:
        corrected_map = {}
        letter_counts = Counter("".join(signals))
        count_to_letters = defaultdict(list)
        for letter, count in letter_counts.items():
            count_to_letters[count].append(letter)

        corrected_map["b"] = count_to_letters[6].pop()
        corrected_map["e"] = count_to_letters[4].pop()
        corrected_map["f"] = count_to_letters[9].pop()

        # Find 1
        for signal in signals:
            match len(signal):
                case 2:
                    corrected_map["c"] = signal.replace(corrected_map["f"], "")
                    count_to_letters[8].remove(corrected_map["c"])
                    corrected_map["a"] = count_to_letters[8].pop()

        # Find 4
        for signal in signals:
            match len(signal):
                case 4:
                    corrected_map["d"] = (signal
                                          .replace(corrected_map["b"], "")
                                          .replace(corrected_map["c"], "")
                                          .replace(corrected_map["f"], "")
                                          )
                    count_to_letters[7].remove(corrected_map["d"])
                    corrected_map["g"] = count_to_letters[7].pop()

        bad_to_good = dict((v, k) for k, v in corrected_map.items())

        digits = ""
        for output in outputs:
            corrected_letters = []
            for letter in output:
                corrected_letters.append(bad_to_good[letter])
            corrected_letters.sort()
            digits += seven_segment_map["".join(corrected_letters)]

        total += int(digits)

    print(f"{total=}")
