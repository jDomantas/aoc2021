from helpers import run


def is_complete(board):
    for i in range(5):
        if all(board[i][j] is None for j in range(5)):
            return True
        if all(board[j][i] is None for j in range(5)):
            return True
    return False


def sum_board(board):
    return sum(x for row in board for x in row if x is not None)


def solve(inp):
    lines = inp.splitlines()
    draw = [int(x) for x in lines[0].split(',')]
    boards = (len(lines) - 1) // 6
    steps = []
    for i in range(boards):
        board = lines[i * 6 + 2 : i * 6 + 7]
        board = [
            [int(x) for x in row.split()]
            for row in board
        ]
        for step, num in enumerate(draw):
            for i in range(5):
                for j in range(5):
                    if board[i][j] == num:
                        board[i][j] = None
            if is_complete(board):
                steps.append((step, num, board))
                break
    _, best_num, best_board = min(steps, key = lambda x: x[0])
    print('part 1:', sum_board(best_board) * best_num)
    _, worst_num, worst_board = max(steps, key = lambda x: x[0])
    print('part 2:', sum_board(worst_board) * worst_num)


run(4, solve)
