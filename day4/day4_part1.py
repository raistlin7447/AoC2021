def find_winner(moves, boards):
    for move in moves:
        for board in boards:
            for win in board:
                if move in win:
                    win.remove(move)
                if len(win) == 0:
                    total = sum(sum(i for i in win) for win in board[:5])
                    return total * move

with open("day4_input.txt") as f:
    lines = f.read().split("\n\n")
    moves = list(map(int, lines[0].split(",")))
    boards = []
    for board in lines[1:-1]:
        rows = [list(map(int, row.split())) for row in board.split("\n")]
        cols = [[row[col] for row in rows] for col in range(len(rows[0]))]
        boards.append(rows + cols)
    print(find_winner(moves, boards))
