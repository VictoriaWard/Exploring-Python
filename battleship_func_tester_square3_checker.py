# battleship test file
# contains square3_checker function
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
                    
    
        
   

ship1 = battleships("The Black Pearl", 1, None, None, None, None, None, None)          #creates ships as instances of battleships class
ship2 = battleships("The Inferno", 1, None, None, None, None, None, None)   
ship3 = battleships("Jolly Roger", 2, None, None, None, None, None, None)              
ship4 = battleships("The Walrus", 3, None, None, None, None, None, None)

