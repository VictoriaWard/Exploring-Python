# battleship.py
# by Victoria Ward
# A simple version of the classic battleship game
# Set your difficulty level by choosing board size

from random import randint      #imports randint function to help to generate battleships


def get_cols():
    """ get_cols() -> int

    Gets number of columns from player and returns as int value.
    """

    global num_cols
    num_cols = input("\nHow big's the ocean, how many columns be she? (minimum 4) ")
    while str.isdigit(num_cols) == False or int(num_cols) < 4:                  #checks player has entered number greater than or equal to 4
        num_cols = input("\nTell me the number of columns? (minimum 4) ")
    return int(num_cols)



def get_rows():
    """ get_rows() -> int

    Gets number of rows from player and returns as int value.
    """

    num_rows = input("\nHow big's the ocean, how many columns be she? (minimum 4) ")
    while str.isdigit(num_rows) == False or int(num_rows) < 4:                  #checks player has entered number greater than or equal to 4
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

    board = []
    for x in range(num_rows):
        board.append(["O"] * num_cols)
    return board



def print_board(board):
    """

    Displays board list. Does not return anything.
    """
    
    for line in board:
        print (" ".join(line))


class battleships(object):
    def __init__(self, name, num_squares, row, col, hit):
        self.name = name
        self.num_squares = num_squares
        self.row = row = None
        self.col = col = None
        self.hit = hit = False

    def row_generator(self):
        """ row_generator() -> int

        Returns a random row number within the range of board rows.
        """

        return randint(1, num_rows)

    def col_generator(self):
        """ col_generator() -> int

        Returns a random column number within the range of board columns.
        """    
    
        return randint(1, num_cols)

    def square_generator(self, row, col, ship_squares):
        """ (int, int) -> dictionary[newKey] = newValue

        Creates a new key value pair containing a given row number and column number
        and appends this to and returns the ship_squares dictionary.

        >>> square_generator(5, 5, ship_squares)
        {5:5}
        """

        self.row = row
        self.col = col
        self.ship_squares = ship_squares = {}

        ship_squares[row] = col
        return ship_squares

    def check_square(self, row, col, ship_squares):
        """ (int, int, list) -> int, int

        Checks to see if a given square with a given row number and a given column number is already
        in the ship_squares dictionary and generates a new square if it is. Returns the row number
        and column number.
        """

        self.row = row
        self.col = col
        self.ship_squares = ship_squares

        for item in self.ship_squares:
            if self.ship_squares.has_key(row):
                while self.ship_squares[row] == col:
                   row_generator()
                   col_generator()
                   square_generator()
        return row, col


ship1 = battleships("The Black Pearl", 1, None, None, False)          #creates ships as instances of battleships class
ship2 = battleships("The Inferno", 1, None, None, False)   
"""ship3 = battleships("Jolly Roger")              
ship4 = battleships("The Walrus")"""
       

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


def check_guess(row_guess, col_guess, num_rows, num_cols, ship_squares):
    """ check_guess(int, int, list) -> string

    Checks that row number guess and column number guess are within the number of board rows and number of column rows limits
    and prints statement if they are not.
    Checks if row number guess and column number guess have been selected previously and prints statement if they have.
    Checks row number guess and column number guess against ship squares list and prints a hit statement if there is a match.
    """
    
    if row_guess < 1 or row_guess > num_rows or col_guess < 1 or col_guess > num_cols:      #checks that player guesses within board limits       
        print ("\nTry firing at the water!")

    elif board[(row_guess-1)][(col_guess-1)] == "X" or board[(row_guess-1)][(col_guess-1)] == "*":         #checks that player has not already guessed here                  
        print ("\nWhat's the matter, matey, ye lost yer mind? Ye just shot thur.")

    elif row_guess == ship1.row and col_guess == ship1.col:                 #checks for a correct guess
        print ("\nArgh there she goes,", ship1.name,"! A fine ship she war... Not bad,", user,"!")
        board[(row_guess - 1)][(col_guess - 1)] = "*"       #updates board to display hit battleship
        ship1.hit = True
        
    elif row_guess == ship1.row and col_guess == ship1.col: 
        print ("\nArgh there she goes,", ship2.name,"! A fine ship she war... Not bad,", user,"!")
        board[(row_guess - 1)][(col_guess - 1)] = "*"
        ship2.hit = True

    else:
        print ("\nBad shot, matey!")                        #dispays miss message if player fails to hit battleship
        board[(row_guess - 1)][(col_guess - 1)] = "X"       #updates board to display guessed square

    return board
        
    """
    elif guess_ship_square == ship_square3:
        print ("\nArgh there she goes,", ship3.ship_name,"! A fine ship she war... Not bad,", user,"!")
        board[(row_guess - 1)][(col_guess - 1)] = "*"
        
        hit3 = True
    elif guess_ship_square == ship_square4:
        print ("\nArgh there she goes,", ship4.ship_name,"! A fine ship she war... Not bad,", user,"!")
        board[(row_guess - 1)][(col_guess - 1)] = "*"
        hit4 = True
    """
        

#create loop/function so that player has option to continue play after each game!!!



user = input("Welome to Battleship, Pirate! What do we call ye? ")      #gets user name

print ("\nAlright", user, "matey... let's see what yer got! ")          #starts game

 
num_cols = get_cols()                               #gets number of clumns and number of rows from player
num_rows = get_rows()

board = board_generator(num_rows, num_cols)                         #creates the board

ship_squares = {}                                   #creates an empty dictionary to store ship coordinates as key value pairs

ship1.row = ship1.row_generator()                   #positions ship1
ship1.col = ship1.col_generator()
ship1.square_generator(ship1.row, ship1.col, ship_squares)          #adds ship1 coordinates to dictionary

ship2.row = ship1.row_generator()                   #positions ship2
ship2.col = ship1.col_generator()
ship2.square_generator(ship2.row, ship2.col, ship_squares)          #adds ship2 coordinates to dictionary
ship2.check_square(ship2.row, ship2.col, ship_squares)              #checks ship2 coordinates do not overlap another ship

guess = 1                                           #assigns value of 1 to guess variable. player is allowed 10 guesses

print ("\nAlrighty, that be the ocean, where be me ships then matey?")

while guess <= 10:                                  #continues game up to ten guesses
    print_board(board)                              #dispays board
    row_guess = get_row_guess()                     #assigns guessed rows and columns to global variables
    col_guess = get_col_guess()
    check_guess(row_guess, col_guess, num_rows, num_cols, ship_squares)     #runs check guess function to check guess location against ship locations and update board
    if ship1.hit == ship2.hit == True:              #checks if player has won and ends game
        print ("\nSHIVER ME TIMBERS! YE DONE IT!")
        break
    if guess <= 10:
        print ("\nShots left: ",(10 - guess))       #displays number of remaining guesses                                       
    guess += 1                                      #updates number of guesses
    if guess > 10:                                  #dispays game over message if player has had ten guesses
        print ("\nGAME OVER!")
        print_board(board)



