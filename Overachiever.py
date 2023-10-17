import GridManager as gm
import copy


def move(length, smart, board, row, col, total_moves=0):
    max_score = (length ** 2) - 1
    # gm.print_board(board, row, col)
    path_found, path, total_moves = find_path(
        board, row, col, smart, total_moves, [], max_score)

    if path_found:
        return total_moves, ', '.join(path)
    else:
        print('No path found. Starting again...')
        board, row, col = start_game(length)
        return move(length, smart, board, row, col, total_moves)


def get_moves(board, row, col, smart):
    search_moves = {'w', 'd', 's', 'a'}
    moves = []
    for x in search_moves:
        if gm.can_move(x, row, col, board, smart):
            moves.append(x)

    return moves


def start_game(length):
    return gm.build_board(length, True)


def evaluate_board(board):
    for i in board:
        for j in i:
            if j:
                return False
    return True


def find_path(board, row, col, smart, total_moves, path, max_depth):
    total_moves += 1
    moves = get_moves(board, row, col, smart)

    if len(moves) == 0 or len(path) >= max_depth:
        return evaluate_board(board), path, total_moves

    for x in moves:
        path.append(x)
        tempBoard, tRow, tCol, tScore = gm.make_move(
            x, copy.deepcopy(board), row, col)
        path_found, path, total_moves = find_path(
            tempBoard,
            tRow,
            tCol,
            smart,
            total_moves,
            copy.deepcopy(path),
            max_depth
        )

        if path_found:
            return True, path, total_moves
        else:
            path.pop()

    return False, path, total_moves
