import GridManager as gm


def move(length, smart, board, row, col):
    max_score = (length ** 2) - 1
    score = 0
    moves_made = 0
    attempts_made = 1
    start_game(board, row, col)

    while score < max_score:
        if moves_made >= max_score:
            print('Max moves exceeded! Try again!')
            board, row, col = gm.build_board(length, True)
            start_game(board, row, col)
            moves_made = 0
            attempts_made += 1
            score = 0

        if (not smart or gm.has_moves_left(board, row, col)):
            move_dir = input()

            if gm.can_move(move_dir, row, col, board, smart):
                board, row, col, move_score = gm.make_move(
                    move_dir, board, row, col)
                score += move_score
                moves_made += 1
                gm.print_board(board, row, col)
            else:
                print("Can't do that, try again.")
        else:
            print('No moves left, restarting...')
            board, row, col = gm.build_board(length, True)
            start_game(board, row, col)
            moves_made = 0
            attempts_made += 1
            score = 0

    return attempts_made


def start_game(board, row, col):
    gm.print_board(board, row, col)
    print(
        """
        The goal is to hit every square without repeating moves.
        You are the "P". Use the WASD keys to move.
        Good luck!"""
    )
