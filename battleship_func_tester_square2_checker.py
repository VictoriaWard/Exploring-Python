# battleship test file
#contains square2_checker function
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
    
        
   

ship1 = battleships("The Black Pearl", 1, None, None, None, None, None, None)          #creates ships as instances of battleships class
ship2 = battleships("The Inferno", 1, None, None, None, None, None, None)   
ship3 = battleships("Jolly Roger", 2, None, None, None, None, None, None)              
ship4 = battleships("The Walrus", 3, None, None, None, None, None, None)

