# David James K Stull
# Computer Science 127

# Logic variables are stored below.
Row = 6
Column = 7
Size = 6 * 7


def clear_board():
    '''
    Creates and returns an empty board with 7 columns and 6 rows.

    A board is empty if it contains only zeros.  During play, cells
    controlled by player 1 will get the value 1, and cells controlled by
    player 2 will get the value 2.
    '''

    board = []
    for i in range(Row):
        board.append([" "] * Column)
    return board


def print_board(board):
    '''
    Prints board with column headers above.  Player 1's tokens should be
    rendered with an 'x', player 2's tokens should be rendered with an 'o',
    and unplayed cells should be rendered with a space.  The column headers
    should be a-g, left to right.  The following is an example of a printed
    board and column headers in a drawn final position:

    abcdefg
    xxooxxx
    oxxxoxo
    oxooooo
    xoxoxox
    xooxxoo
    xxoxoxo
    '''

    for k in range(Row - 1, -1, -1):
        print("  " + ' '.join(board[k]))
    for k in range(Column):
        if k == 0:
            print("  " + str(k) + " ", end='')
        else:
            print(str(k) + " ", end='')
    print()


def choose_token():
    """
    Allows player one to decide if they want to be X or O.
    Make sure you let the person you play with be player one sometimes. Be fair.
    """
    myturn = ""
    while (myturn != "X" and myturn != "O"):
        print("Player 1. Would you like to be X or O?")
        myturn = input().upper()

    return myturn


def is_valid_move(index, board, Turn):
    """
    This function allows the simulation to determine if a valid move can be made.
    """

    for k in board:
        if k[index] == " ":
            k[index] = Turn
            # Size -= 1
            return True
    return False


def read_move(turn):

    # This function kind of has the combined functionality of is_open, has_open, and drop_token.

    '''
    Prompts player for a move.  Reads a column name, 0-6, from the
    terminal.  Retries in the case of erroneous input.  Returns an
    integer in the range [0,6] corresponding to a-g respectively.

    Hint: Use ord() to convert a letter to an integer.
          ord(column) - ord('a') will give a "distance from 'a'".
    '''

    index = -1
    while not (0 <= index <= 6):
        print("Player " + turn + ". Where would you like to drop your token from 0 to 6?")
        try:
            index = int(input())
        except ValueError:
            print("Invalid Input")
            continue
        else:
            continue
    return index



# For efficency, is_open, has_open, and drop_token have all been implemented into other functions.



def play_turn(Turn):
    '''
    Reads player's move from the terminal (calls read_move()).  If the
    move is valid, calls drop_token() to update the board, otherwise
    read_move() is called until the move is valid.  Returns the updated
    board.
    '''

    if Turn == "X":
        return "O"
    return "X"


def player_wins(board, turn):
    '''
    Returns winner if and only if there is a four-in-a-row passing
    through the position at column and row in any direction.
    '''

    # Check for Horizontal win.
    for x in range(Row):
        for y in range(Column - 3):
            if board[x][y] == turn and board[x][y + 1] == turn and board[x][y + 2] == turn and board[x][y + 3] == turn:
                return turn + " wins!"

    # Check for Verticle win.
    for y in range(Column):
        for x in range(Row - 3):
            if board[x][y] == turn and board[x + 1][y] == turn and board[x + 2][y] == turn and board[x + 3][y] == turn:
                return turn + " wins!"

    # Check for Diagonal win.
    for x in range(Column - 3):
        for y in range(Row - 3):
            if board[x][y] == turn and board[x + 1][y + 1] == turn and board[x + 2][y + 2] == turn and board[x + 3][
                y + 3] == turn:
                return turn + " wins!"

    # Check for Diagonal win.
    for x in range(Column - 3):
        for y in range(3, Row):
            if board[x][y] == turn and board[x + 1][y - 1] == turn and board[x + 2][y - 2] == turn and board[x + 3][
                y - 3] == turn:
                return turn + " wins!"
    return None


def play_game():
    """
    Configures and plays one game of Connect 4.
    """
    First = choose_token()
    Second = ""
    Turn = First
    winner = None
    numberpiece = 0  # for count tie game

    if First == "X":
        Second = "O"
    else:
        Second = "X"

    board = clear_board()

    while True:
        print_board(board)
        index = read_move(Turn)
        if is_valid_move(index, board, Turn):
            numberpiece += 1
            winner = player_wins(board, Turn)
            Turn = play_turn(Turn)
        else:
            print("ERROR: Move invalid for player " + Turn)

        if winner != None:
            print_board(board)
            print(winner)
            break
        if numberpiece == Size:
            print_board(board)
            print("It's a Tie! Isn't that just life in a nutshell. All this work for it just to be a tie.")
            break

if __name__ == '__main__':
    play_game()