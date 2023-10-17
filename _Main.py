from BigBrain import BigBrain
import GridManager as gm
import User as player
import Dummy as dummy
import Underachiever as under
import Overachiever as over
from Overachiever_Streamlined import Overachiever_Streamlined

board = []
sideLength = None
max_moves = -1

testing = input("""
Who would you like to test? (Supports multiple, or * for all)
    1 - Player
    2 - Dummy
    3 - Better Dummy
    4 - Underachiever
    5 - Overachiever
    6 - Better Overachiever
    7 - Best Overachiever
    8 - Learner
""")

if __name__ == "__main__":
    while True:
        while (sideLength is None):
            sideLength = gm.try_parse_int(input('How many squres to a side? '))

        board, row, col = gm.build_board(sideLength, False)
        gm.print_board(board, row, col)

        # Human
        if testing.find('1') != -1:
            attempts_made = player.move(sideLength, False, board, row, col)
            print('Attempts made by Player to reach perfect path: {:,}'.format(
                attempts_made))

        # Dummy
        if testing == '*' or testing.find('2') != -1:
            attempts_made = dummy.move(
                sideLength, False, True, board, row, col)
            print('Attempts made by Dummy to reach perfect path: {:,}'.format(
                attempts_made))

        if testing == '*' or testing.find('3') != -1:
            attempts_made = dummy.move(sideLength, True, True, board, row, col)
            print('Better Dummy attempts: {:,}'.format(attempts_made))

        # Underachiever
        if testing == '*' or testing.find('4') != -1:
            attempts_made = under.move(sideLength, True, board, row, col)
            print('Underachiever attempts: {:,}'.format(attempts_made))

        # Overachiever
        if testing == '*' or testing.find('5') != -1:
            moves_searched, path = over.move(
                sideLength, False, board, row, col)
            print('Overachiever moves searched: {:,}'.format(moves_searched))
            print('Path Found: ' + path)

        # Better Overachiever
        if testing == '*' or testing.find('6') != -1:
            moves_searched, path = over.move(sideLength, True, board, row, col)
            print('Better Overachiever moves searched: {:,}'.format(
                moves_searched))
            print('Path Found: ' + path)

        # Best Overachiever
        if testing == '*' or testing.find('7') != -1:
            over2 = Overachiever_Streamlined(True, (sideLength ** 2) - 1)
            moves_searched, path = over2.move(board, row, col)
            print('Best Overachiever moves searched: {:,}'.format(
                moves_searched))
            print('Path Found: ' + path)

        if testing == '*' or testing.find('8') != -1:
            brain = BigBrain()
            path = brain.solve(max_moves=(
                sideLength ** 2 - 1), sides=sideLength)
            print('Path found: ', path)

        if input('try again? y/n: ').lower() == 'y':
            sideLength = None
        else:
            break

    print('')
    print('Thanks for playing!')
