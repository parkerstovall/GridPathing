import GridManager as gm
import random as rand


def move(length, smart, useRand, board, row, col):
    max_score = (length ** 2) - 1
    score = 0
    moves_made = 0
    attempts_made = 1

    while score < max_score:
        if moves_made >= max_score:
            board, row, col = gm.build_board(length, useRand)
            moves_made = 0
            attempts_made += 1
            score = 0

        if (not smart or gm.has_moves_left(board, row, col)):
            move_dir = ''
            num = rand.randint(0, 3)

            if num == 0:
                move_dir = 'w'
            elif num == 1:
                move_dir = 'd'
            elif num == 2:
                move_dir = 's'
            else:
                move_dir = 'a'

            if gm.can_move(move_dir, row, col, board, smart):
                board, row, col, move_score = gm.make_move(
                    move_dir, board, row, col)
                score += move_score
                moves_made += 1
        else:
            board, row, col = gm.build_board(length, useRand)
            moves_made = 0
            attempts_made += 1
            score = 0

    return attempts_made
