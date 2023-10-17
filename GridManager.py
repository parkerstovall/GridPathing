import random as rand
import time


def try_parse_int(value):
    try:
        if (len(value.strip()) > 0):
            return int(value)
        else:
            return None
    except ValueError:
        return None


def get_curr_time():
    return round(time.time() * 1000)


def build_board(length, useRand):
    board = []
    for i in range(length):
        board.append([])
        for j in range(length):
            board[i].append(True)
    return drop_player(board, useRand)


def drop_player(board, useRand):
    if useRand:
        length = len(board) - 1
        row = rand.randint(0, length)
        col = rand.randint(0, length)
    else:
        row = 0
        col = 0
    board[row][col] = False
    return board, row, col


def print_board(board, pRow, pCol):
    output = '\n\n'
    for i in range(len(board)):
        for j in range(len(board[i])):
            if pRow == i and pCol == j:
                output += 'P, '
            elif board[i][j]:
                output += 'O, '
            else:
                output += 'X, '
        output += '\n'
    print(output)


def has_moves_left(board, row, col):
    inc = {-1, 1}
    length = len(board)

    for i in inc:
        if row + i < length and row + i >= 0 and board[row + i][col]:
            return True
        elif col + i < length and col + i >= 0 and board[row][col + i]:
            return True

    return False


def get_inc(move_dir):
    if (move_dir == 'w'):
        return -1, 0
    elif (move_dir == 'a'):
        return 0, -1
    elif (move_dir == 's'):
        return 1, 0
    elif (move_dir == 'd'):
        return 0, 1
    return 0, 0


def is_in_board(row, col, length=8):
    return (
        row >= 0
        and row < length
        and col >= 0
        and col < length
    )


def can_move(move_dir, row, col, board, smart):
    rowInc, colInc = get_inc(move_dir)

    row += rowInc
    col += colInc

    if not is_in_board(row, col, len(board)):
        return False
    elif not smart:
        return True
    else:
        return board[row][col]


def make_move(move_dir, board, row, col):
    if move_dir == 'w':
        row -= 1
    elif move_dir == 'a':
        col -= 1
    elif move_dir == 's':
        row += 1
    elif move_dir == 'd':
        col += 1

    move_score = -1
    if board[row][col]:
        move_score = 1
        board[row][col] = False

    return board, row, col, move_score
