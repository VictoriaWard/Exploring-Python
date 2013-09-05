# battleship test file
# file containing check_guess functions
# Victoria Ward

num_rows = 5
num_cols = 5

ship_squares = ["1,1", "2,2", "3,1", "3,2", "4,1", "4,2", "4,3"]
board = [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]
hit_squares = []


class battleships(object):
    def __init__(self, name, num_squares, row, col, row2, col2, row3, col3):
        self.name = name
        self.num_squares = num_squares
        self.row = row = None
        self.col = col = None
        self.row2 = row2 = None
        self.col2 = col2 = None
        self.row3 = row3 = None
        self.col3 = col3 = None

ship1 = battleships("The Black Pearl", 1, None, None, None, None, None, None)          #creates ships as instances of battleships class
ship2 = battleships("The Inferno", 1, None, None, None, None, None, None)   
ship3 = battleships("Jolly Roger", 2, None, None, None, None, None, None)              
ship4 = battleships("The Walrus", 3, None, None, None, None, None, None)



def check_on_board(row_guess, col_guess):
    """check_on_board(int, int) -> Boolean

    Returns True if row and column guess numbers are within range of board rows and columns. 

    >>>check_on_board(0, 3)
    False
    >>>check_on_board(3, 6)
    False
    >>>check_on_board(3, 3)
    True
    """

    return (1 <= row_guess <= (num_rows)) and (1 <= col_guess <= (num_cols))


def if_guessed(row_guess, col_guess, board):
    """if_guessed(int, int, list) -> Boolean

    Returns True if square has been guessed before( ie. if the row and column guess numbers are the same as a row and column number in the
    board list characterised with "X" or "*").

    Assumes guess_row and guess_col are within range of board rows and columns.

    >>>if_guessed(1, 1, board = [['X', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O']])
    True
    >>>if_guessed(1, 2, board = [['X', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O']])
    False
    >>>if_guessed(3, 3, board = [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', '*', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O']])
    True
    >>>if_guessed(2, 3, board = [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', '*', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O']])
    False
    """

    return board[(row_guess-1)][(col_guess-1)] == "X" or board[(row_guess-1)][(col_guess-1)] == "*" 
    
    
def check_hit(row_guess, col_guess, ship_squares):
    """check_hit(int, int, list) -> Boolean

    Returns true if there is a match between guess row and column numbers and ship_squares list of ship rows and columns.

    Assumes guess_row and guess_col are within range of board rows and columns.

    >>>check_hit(3, 3, ship_squares = ["1,1", "2,2", "3,1", "3,2", "4,1", "4,2", "4,3"])
    False
    >>>check_hit(1, 1, ship_squares = ["1,1", "2,2", "3,1", "3,2", "4,1", "4,2", "4,3"])
    True
    """

    row_guess = str(row_guess)
    col_guess = str(col_guess)
    square = row_guess + "," + col_guess

    return square in ship_squares


def add_to_hit_squares(row_guess, col_guess, hit_squares):
    """add_to_hit_squares(int, int, list) -> list

    Adds the successful row and column guess numbers to the hit_squares list.

    Assumes that row and column guess numbers are not already in list.

    >>>add_to_hit_squares(1, 1, hit_squares = [])
    ["1,1"]
    >>>add_to_hit_squares(3, 4, hit_squares = ["1,1"])
    ["1,1", "3,4"]
    """

    row_guess = str(row_guess)
    col_guess = str(col_guess)
    square = row_guess + "," + col_guess

    hit_squares.append(square)
    return hit_squares

    
def check_win(hit_squares, ship_squares):
    """check_win(list, list) -> Boolean

    Returns True if hit_squares list and ship_squares list contain exactly the same items.

    >>>check_win(hit_squares = ["1,1", "2,2"], ship_squares = ["1,1", "2,2", "3,1", "3,2", "4,1", "4,2", "4,3"])
    False
    >>>check_win(hit_squares = ["1,1", "2,2", "3,1", "3,2", "4,1", "4,2", "4,3"], ship_squares = ["1,1", "2,2", "3,1", "3,2", "4,1", "4,2", "4,3"])
    True
    """
    return hit_squares == ship_squares
    

def update_hit(row_guess, col_guess, board):
    """update_hit(int, int, list) -> list

    Updates the string saved in the board list indexes that correspond with the successful row and column guess coordinates to "*".

    Assumes that this value is not alreadys "*".

    >>>update_hit(1, 1, board = [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O']])
    [['*', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]
    >>>update_hit(3, 3, board = [['*', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O']])
    [['*', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', '*', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]
    """

    board[(row_guess - 1)][(col_guess - 1)] = "*"
    return board


def update_miss(row_guess, col_guess, board):
    """update_miss(int, int, list) -> list

    Updates the string saved in the board list indexes that correspond with the unsuccessful row and column guess coordinates to "X".

    Assumes that this value is not alreadys "X".

    >>>update_miss(1, 1, board = [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O']])
    [['X', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]
    >>>update_miss(3, 3, board = [['X', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O']])
    [['X', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'X', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]
    """

    board[(row_guess - 1)][(col_guess - 1)] = "X"
    return board
    
       
def check_guess(row_guess, col_guess, hit_squares, ship_squares, board):
    """check_guess(int, int, list, list, list) -> string, list

    May return one or more of the above types.

    >>>check_guess(3, 3, hit_squares = [], ship_squares = ["1,1", "2,2", "3,1", "3,2", "4,1", "4,2", "4,3"], board = [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']])
    "Miss!"
    [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'X', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]
    >>>check_guess(3, 3, hit_squares = [], ship_squares = ["1,1", "2,2", "3,1", "3,2", "4,1", "4,2", "4,3"], board = [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']])
    "Miss!"
    [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'X', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]
    >>>check_guess(0, 3, hit_squares = [], ship_squares = ["1,1", "2,2", "3,1", "3,2", "4,1", "4,2", "4,3"], board = [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'X', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']])
    "\nTry firing at the water!"
    >>>check_guess(1, 7, hit_squares = [], ship_squares = ["1,1", "2,2", "3,1", "3,2", "4,1", "4,2", "4,3"], board = [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'X', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']])
    "\nTry firing at the water!"
    >>>check_guess(1, 1, hit_squares = [], ship_squares = ["1,1", "2,2", "3,1", "3,2", "4,1", "4,2", "4,3"], board = [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'X', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']])
    "Argh, it's a hit!"
    [['*', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'X', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]
    {1:1}
    >>>check_guess(3, 3, hit_squares = [], ship_squares = ["1,1", "2,2", "3,1", "3,2", "4,1", "4,2", "4,3"], board = [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'X', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']])
    "What's the matter, matey, ye lost yer mind? Ye just shot thur."
    [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'X', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]
    >>>check_guess(4, 3, hit_squares = ["1,1", "2,2", "3,1", "3,2", "4,1", "4,2", "4,3"], ship_squares = ["1,1", "2,2", "3,1", "3,2", "4,1", "4,2", "4,3"], board = [['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'X', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']])
    "SHIVER ME TIMBERS! YE DONE IT! YE WON!"
    [['*', 'O', 'O', 'O', 'O'], ['O', '*', 'O', 'O', 'O'], ['*', '*', 'X', 'O', 'O'],
    ['*', '*', '*', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]
    {1:1, 2:2, 3:1, 3:2, 4:1, 4:2, 4:3}
    """

    if not check_on_board(row_guess, col_guess):
        print("\nTry firing at the water!")
    elif if_guessed(row_guess, col_guess, board):
        print ("\nWhat's the matter, matey, ye lost yer mind? Ye just shot thur.")
    elif check_hit(row_guess, col_guess, ship_squares):
        print ("\nArgh, it's a hit!")
        update_hit(row_guess, col_guess, board)
        add_to_hit_squares(row_guess, col_guess, hit_squares)
        if check_win(hit_squares, ship_squares):
            print ("\nSHIVER ME TIMBERS! YE DONE IT! YE WON!")
    else:
        print ("\nMiss!")
        update_miss(row_guess, col_guess, board)

    return board

     
               
               
               
        
    
    
    
        
    
