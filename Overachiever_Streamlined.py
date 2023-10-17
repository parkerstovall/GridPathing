import GridManager as gm


class Overachiever_Streamlined:
    def __init__(self, smart, max_depth):
        self.total_moves_test = 0
        self.smart = smart
        self.max_depth = max_depth
        self.opp_moves = {"w": "s", "a": "d", "s": "w", "d": "a"}

    def move(self, board, row, col):
        length = len(board)
        rowMin = min(row, length - (row + 1))
        colMin = min(col, length - (col + 1))
        vert = horiz = ""

        if row < length - (row + 1):
            vert = 'w'
        else:
            vert = 's'

        if col < length - (col + 1):
            horiz = 'a'
        else:
            horiz = 'd'

        if rowMin == colMin and rowMin != 1:
            self.search_moves = [self.opp_moves[vert],
                                 self.opp_moves[horiz], vert, horiz]

        elif rowMin == 0 or row == length - 1:
            self.search_moves = [vert, horiz,
                                 self.opp_moves[vert], self.opp_moves[horiz]]

        elif colMin == 0 or col == length - 1:
            self.search_moves = [horiz, vert,
                                 self.opp_moves[horiz], self.opp_moves[vert]]

        elif rowMin > colMin:
            self.search_moves = [vert, horiz,
                                 self.opp_moves[vert], self.opp_moves[horiz]]

        else:
            self.search_moves = [horiz, vert,
                                 self.opp_moves[horiz], self.opp_moves[vert]]

        path_found, path = self.find_path(board, row, col, [], 0)

        if path_found:
            return self.total_moves_test, ', '.join(path)
        else:
            print('No path found. Starting again...')
            board, row, col = self.start_game(length)
            return self.move(board, row, col)

    def get_moves(self, board, row, col, path):
        search_moves = self.search_moves

        if path:
            badmove = self.opp_moves[path[-1]]
        else:
            badmove = 'x'

        moves = []
        for x in search_moves:
            if x != badmove and gm.can_move(x, row, col, board, self.smart):
                moves.append(x)

        return moves

    def start_game(self, length):
        return gm.build_board(length, True)

    def find_path(self, board, row, col, path, depth):
        self.total_moves_test += 1
        moves = self.get_moves(board, row, col, path)

        if depth == self.max_depth:
            return True, path

        for x in moves:
            path.append(x)
            tempBoard, tRow, tCol, score = gm.make_move(x, board, row, col)
            path_found, path = self.find_path(
                tempBoard, tRow, tCol, path, depth + 1)
            board[tRow][tCol] = True

            if path_found:
                return True, path
            else:
                path.pop()

        return False, path
