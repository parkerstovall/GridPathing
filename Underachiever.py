import GridManager as gm


def move(length, useRand, board, row, col):
    max_score = (length ** 2) - 1
    score = 0
    moves_made = 0
    attempts_made = 1
    # gm.print_board(board, row, col)
    move_dir = 'w'

    while score < max_score:
        if moves_made >= max_score:
            board, row, col = gm.build_board(length, useRand)
            moves_made = 0
            attempts_made += 1
            score = 0

        if (gm.has_moves_left(board, row, col)):
            if gm.can_move(move_dir, row, col, board, True):
                board, row, col, move_score = gm.make_move(
                    move_dir, board, row, col)
                score += move_score
                moves_made += 1
            else:
                move_dir = rotate(move_dir)
        else:
            board, row, col = gm.build_board(length, useRand)
            moves_made = 0
            attempts_made += 1
            score = 0

    return attempts_made


def rotate(move_dir):
    if move_dir == 'w':
        return 'd'
    elif move_dir == 'd':
        return 's'
    elif move_dir == 's':
        return 'a'
    else:
        return 'w'
