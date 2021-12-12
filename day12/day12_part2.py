from collections import defaultdict

locations = defaultdict(list)

def find_paths(node, visited = None, lower_twice = False):
    if visited is None:
        visited = []
    if node == "end":
        return [visited]
    total = []
    for next in locations[node]:
        if next == "start":
            continue
        if next in visited and lower_twice:
            continue
        if next in visited:
            if node.islower():
                total += find_paths(next, visited + [node], True)
            else:
                total += find_paths(next, visited, True)
        else:
            if node.islower():
                total += find_paths(next, visited + [node], lower_twice)
            else:
                total += find_paths(next, visited, lower_twice)
    return total

with open("day12_input.txt") as f:
    lines = list(map(str.strip, f.readlines()))
    connections = [line.split("-") for line in lines]

    for start, end in connections:
        if end not in locations[start]:
            locations[start].append(end)
        if start not in locations[end]:
            locations[end].append(start)

    paths = find_paths("start")
    print(len(paths))
