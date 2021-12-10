from collections import deque

with open("day10_input.txt") as f:
    lines = list(map(str.strip, f.readlines()))

    open_char = ["(", "[", "{", "<"]
    close_char = [")", "]", "}", ">"]
    score_map = {")": 1, "]": 2, "}": 3, ">": 4}

    scores = []
    for line in lines:
        stack = deque()
        corrupt = False
        for char in line:
            if char in open_char:
                stack.append(char)
            if char in close_char:
                open_match = open_char[close_char.index(char)]
                if stack.pop() != open_match:
                    corrupt = True
                    break
        if corrupt:
            continue
        score = 0
        while stack:
            unclosed = stack.pop()
            close_match = close_char[open_char.index(unclosed)]
            score = score * 5 + score_map[close_match]
        scores.append(score)
    scores.sort()
    middle = scores[int(len(scores)/2)]
    print(f"{middle=}")
