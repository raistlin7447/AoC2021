##### Original Solution #####
def find_loser(moves, boards):
    for move in moves:
        new_boards = []
        for board in boards:
            has_won = False
            for win in board:
                if move in win:
                    win.remove(move)
                if len(win) == 0:
                    has_won = True
                    break
            if not has_won:
                new_boards.append(board)
        if len(new_boards) == 0:
            total = sum(sum(i for i in win) for win in board[:5])
            return total * move
        boards = new_boards

with open("day4_input.txt") as f:
    lines = f.read().split("\n\n")
    moves = list(map(int, lines[0].split(",")))
    boards = []
    for board in lines[1:-1]:
        rows = [list(map(int, row.split())) for row in board.split("\n")]
        cols = [[row[col] for row in rows] for col in range(len(rows[0]))]
        boards.append(rows + cols)
    print(find_loser(moves, boards))

##### Alternate solution with just sorting boards. #####
with open("day4_input.txt") as f:
    lines = f.read().split("\n\n")
    moves = list(map(int, lines[0].split(",")))

    # Build Board
    boards = []
    for board in lines[1:-1]:
        rows = [list(map(int, row.split())) for row in board.split("\n")]
        cols = [[row[col] for row in rows] for col in range(len(rows[0]))]
        boards.append(rows + cols)

    # Sort Boards
    sorted_boards = []
    for move in moves:
        new_boards = []
        for board in boards:
            for win in board:
                if move in win:
                    win.remove(move)
                if len(win) == 0:
                    result_score = sum(sum(i for i in win) for win in board[:5]) * move
                    sorted_boards.append(result_score)
                    break
            else:
                new_boards.append(board)
        boards = new_boards
    
    print(sorted_boards[0])     # Part 1
    print(sorted_boards[-1])    # Part 2
