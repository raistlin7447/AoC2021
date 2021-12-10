from collections import deque

with open("day10_input.txt") as f:
    lines = list(map(str.strip, f.readlines()))

    open_char = ["(", "[", "{", "<"]
    close_char = [")", "]", "}", ">"]
    score_map = {")": 3, "]": 57, "}": 1197, ">": 25137}

    total = 0
    for line in lines:
        stack = deque()
        for char in line:
            if char in open_char:
                stack.append(char)
            if char in close_char:
                open_match = open_char[close_char.index(char)]
                if stack.pop() != open_match:
                    total += score_map[char]
                    break
    print(f"{total=}")
