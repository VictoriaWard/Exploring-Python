# battleship.py
# by Victoria Ward
# A simple version of the classic battleship game
# Set your difficulty level by choosing board size


from random import randint      #imports randint function to help to generate battleships


def get_cols():
    """ get_cols() -> int

    Gets number of columns from player and returns as int value.
    """

    num_cols = input("\nHow big's the ocean, how many columns be she? (minimum 4) ")
    while str.isdigit(num_cols) == False or int(num_cols) < 4:                    #checks player has entered number greater than or equal to 4
        num_cols = input("\nTell me the number of columns? (minimum 4) ")
    return int(num_cols)


def get_rows():
    """ get_rows() -> int

    Gets number of rows from player and returns as int value.
    """

    num_rows = input("\nHow big's the ocean, how many columns be she? (minimum 4) ")
    while str.isdigit(num_rows) == False or int(num_rows) < 4:                    #checks player has entered number greater than or equal to 4
        num_rows = input("\nTell me the number of columns? (minimum 4) ")
    return int(num_rows)


def board_generator(num_rows, num_cols):
    """ board_generator(int, int) -> new list

    Calculates board size and returns a board list for a given number
    of rows and number of columns.

    >>>board_genartor(5, 5)
    [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]
    >>>board_generator(4, 4)
    [['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O']]
    >>>board_generator(6, 4)
    [['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O'],  ['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O']]
    """
    
    for x in range(num_rows):
        board.append(["O"] * num_cols)
    return board


def print_board(board):
    """

    Displays board list as a board of "O"s. Does not return anything.
    """
    
    for line in board:
        print (" ".join(line))


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

    def row_generator(self):
        """ row_generator() -> int

        >>>ship1.row_generator()
        n      #n is a random integer between 1 and the number of rows

        Returns a random row number within the range of board rows.
        """

        return randint(1, num_rows)

    def col_generator(self):
        """ col_generator() -> int

        >>>ship1.col_generator()
        n      #n is a random integer between 1 and the number of columns

        Returns a random column number within the range of board columns.
        """    
    
        return randint(1, num_cols)

    def ship_square_checker(self, x, y, ship_squares):
        """ (int, int) -> list

        >>>ship1.ship_square_checker(5, 5, ship_squares = [])
        ["5,5"]
        >>>ship1.ship_square_checker(5, 5, ship_squares = ["5,5"])
        ["5,5"]
        >>>ship1.ship_square_checker(2, 3, ship_squares = ["5,5"])
        ["2,3", "5,5"]

        Creates new key value pair containing given ship's row and column numbers
        and appends this to ship_squares list if not already in list. returns ship_squares list.
        """

        self.x = x        
        self.y = y
        self.ship_squares = ship_squares

        x = str(x)
        y = str(y)
        square = x + "," + y
        
        if square in ship_squares:
            ship_squares = ship_squares
        else:
            ship_squares.append(square)
        return ship_squares

    def square2_checker(self, x, y, row2, col2):
        """ (int, int, int, int) -> Boolean

        >>>ship3.square2_checker(5, 5, 1, 3)
        False
        >>>ship3.square2_checker(5, 5, 5, 5)
        False
        >>>ship3.square2_checker(5, 5, 5, 4)
        True
        >>>ship3.square2_checker(5, 5, 4, 5)
        True

        Checks row2 and column2 against row1 and column1 to see if ship square2 is connected to,
        but not the same as, ship square1. In this case returns True.
        """
        
        self.x = x
        self.y = y
        self.row2 = row2
        self.col2 = col2

        return abs(self.x - self.row2) == 1 and self.col2 == self.y \
               or abs(self.y - self.col2) == 1 and self.row2 == self.x

    def square3_checker(self, x, y, row2, col2, row3, col3) :
        """ (int, int, int, int, int, int) -> Boolean

        >>>ship4.square3_checker(3, 3, 3, 2, 1, 1)
        False
        >>>ship4.square3_checker(5, 5, 4, 5, 4, 4)
        False
        >>>ship4.square3_checker(4, 1, 3, 1, 4, 2)
        False
        >>>ship4.square3_checker(3, 3, 3, 2, 3, 2)
        False
        >>>ship4.square3_checker(3, 3, 3, 2, 3, 1)
        True
        >>>ship4.square3_checker(3, 3, 3, 2, 3, 4)
        True
        >>>ship4.square3_checker(5, 1, 4, 1, 3, 1)
        True
        
        Checks row3 and column3 against row1, column1, row 2 and column2 to see if ship square3 is connected to,
        but not the same as, ship square1 or ship square 2 in a line. In this case returns True.
        """
        
        self.x = x
        self.y = y
        self.row2 = row2
        self.col2 = col2
        self.row3 = row3
        self.col3 = col3

        return ((abs(self.row3 - min(self.x, self.row2)) == 1 or \
                   abs(self.row3 - max(self.x, self.row2)) ==1) and \
                    self.row3 != self.x and self.row3 != self.row2) and \
                    self.col3 == self.col2 == self.y or \
                    ((abs(self.col3 - min(self.y, self.col2)) == 1 or \
                      abs(self.col3 - max(self.y, self.col2)) == 1) and \
                     self.col3 != self.y and self.col3 != self.col2 and \
                     self.row3 == self.row2 == self.x)

       
def get_row_guess():
    """ get_row_guess() -> int

    Gets row guess from player and returns as int value.
    """
        
    row = input("\nWhich row? ")              #gets player's row guess
    while str.isdigit(row) == False:          #checks that player has enter a number 
        row = input("\nWhich row I say?")
    return int(row)  


def get_col_guess():
    """ get_col_guess() -> int

    Gets column guess from player and returns as int value.
    """
        
    col = input("\nWhich column? ")           #gets player's column guess
    while str.isdigit(col) == False:          #checks that player has enter a number 
        col = input("\nWhich column I say?")
    return int(col) 


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
        

ship1 = battleships("The Black Pearl", 1, None, None, None, None, None, None)          #creates ships as instances of battleships class
ship2 = battleships("The Inferno", 1, None, None, None, None, None, None)   
ship3 = battleships("Jolly Roger", 2, None, None, None, None, None, None)              
ship4 = battleships("The Walrus", 3, None, None, None, None, None, None)


#create loop/function so that player has option to continue play after each game!!!


user = input("Welome to Battleship, Pirate! What do we call ye? ")      #gets user name

print ("\nAlright", user, "matey... let's see what yer got! ")          #starts game

num_rows = get_rows()                               #gets number of clumns and number of rows from player
num_cols = get_cols()
board = []                                          #creates an empty list to store board
board = board_generator(num_rows, num_cols)         #creates the board

ship_squares = []           #creates an empty dictionary to store ship coordinates as key value pairs
hit_squares = []            #creates an empty dictionary to store successful coordinate guesses as key value pairs

ship1.row = ship1.row_generator()                   #positions ship1
ship1.col = ship1.col_generator()
ship1.ship_square_checker(ship1.row, ship1.col, ship_squares)          #adds ship1 coordinates to dictionary

while len(ship_squares) == 1:
    ship2.row = ship2.row_generator()                   
    ship2.col = ship2.col_generator()
    ship2.ship_square_checker(ship2.row, ship2.col, ship_squares)

while len(ship_squares) == 2:
    ship3.row = ship3.row_generator()                   
    ship3.col = ship3.col_generator()
    ship3.ship_square_checker(ship3.row, ship3.col, ship_squares)
    
while len(ship_squares) == 3:
    ship3.row2 = ship3.row_generator()                   
    ship3.col2 = ship3.col_generator()
    if ship3.square2_checker(ship3.row, ship3.col, ship3.row2, ship3.col2):  #checks ship3 second square connected to first square
        ship3.ship_square_checker(ship3.row2, ship3.col2, ship_squares)
        
while len(ship_squares) == 4:
    ship4.row = ship4.row_generator()                   
    ship4.col = ship4.col_generator()
    ship4.ship_square_checker(ship4.row, ship4.col, ship_squares)
    
while len(ship_squares) == 5:
    ship4.row2 = ship4.row_generator()                   
    ship4.col2 = ship4.col_generator()
    if ship4.square2_checker(ship4.row, ship4.col, ship4.row2, ship4.col2):  #checks ship4 second square connected to first square
        ship4.ship_square_checker(ship4.row2, ship4.col2, ship_squares)

while len(ship_squares) == 6:
    ship4.row3 = ship4.row_generator()                   
    ship4.col3 = ship4.col_generator()
    if ship4.square3_checker(ship4.row, ship4.col, ship4.row2, ship4.col2, ship4.row3, ship4.col3):  #checks ship4 third square connected to first and second squares in a line
        ship4.ship_square_checker(ship4.row3, ship4.col3, ship_squares)


print ("\nAlrighty, that be the ocean, where be me ships then matey?")

for guess in range(10):
    if not check_win(hit_squares, ship_squares):                               #continues game up to ten guesses
        print_board(board)                              #dispays board
        row_guess = get_row_guess()                     #assigns guessed rows and columns to global variables
        col_guess = get_col_guess()
        check_guess(row_guess, col_guess, hit_squares, ship_squares, board)

if not check_win(hit_squares, ship_squares):
    print ("\nGAME OVER! You lose!")
    print_board(board)
    
    



