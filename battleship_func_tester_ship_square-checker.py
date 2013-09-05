# battleship test file
# file containing ship_square-checker functions
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
   

ship1 = battleships("The Black Pearl", 1, None, None, None, None, None, None)          #creates ships as instances of battleships class
ship2 = battleships("The Inferno", 1, None, None, None, None, None, None)   
ship3 = battleships("Jolly Roger", 2, None, None, None, None, None, None)              
ship4 = battleships("The Walrus", 3, None, None, None, None, None, None)
