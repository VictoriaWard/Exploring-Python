# battleship test file
# contains ship placing functions
# Victoria Ward

from random import randint

num_rows = 5
num_cols = 5

board = [['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O'],  ['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O']]




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
        
   

ship1 = battleships("The Black Pearl", 1, None, None, None, None, None, None)          #creates ships as instances of battleships class
ship2 = battleships("The Inferno", 1, None, None, None, None, None, None)   
ship3 = battleships("Jolly Roger", 2, None, None, None, None, None, None)              
ship4 = battleships("The Walrus", 3, None, None, None, None, None, None)







ship_squares = []           #creates an empty list to store ship coordinates as key value pairs
hit_squares = []            #creates an empty list to store successful coordinate guesses as key value pairs




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
       










