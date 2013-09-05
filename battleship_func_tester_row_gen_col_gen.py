# battleship test file
# file containing row and column generator functions
# Victoria Ward

from random import randint

num_rows = 5
num_cols = 5

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

ship1 = battleships("The Black Pearl", 1, None, None, None, None, None, None)          #creates ships as instances of battleships class
ship2 = battleships("The Inferno", 1, None, None, None, None, None, None)    
"""ship3 = battleships("Jolly Roger")              
ship4 = battleships("The Walrus")"""
