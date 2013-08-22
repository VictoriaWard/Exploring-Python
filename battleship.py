# battleship.py
# by Victoria Ward
# A simple version of the classic battleship game
# Choose your board size and number of battleships

from random import randint      #imports randint function to help to generate battleships

user = input("Welome to Battleship, Pirate! What do we call ye?")       #gets user name
print ("Alright", user, "matey... let's see what yer got!")          #starts game

board_col = input("How big's the ocean, how many columns be she? (minimum 4)")      #gets board size, columns
board_col = int(board_col)                  #converts to int for calculations
board_row = input("And how many rows be she? (minimum 4)")          #gets board size, rows
board_row = int(board_row)                  #converts to int for calculations

board_size = board_row * board_col          #calculates board size
if board_size <= 20:                        #comments on chosen difficulty level
    print ("Ha ha ha! Not so tough ey matey!") 
if 21 <= board_size <= 36:
    print ("Think ye tough ey matey!")
if 37 <= board_size <= 49:
    print ("You know somethin' I don't, hotshot?")
if board_size >= 50:
    print ("Crikey! He's a madman!")

board = []                      #creates board            
for x in range(1, board_row):                
    board.append(["O"] * board_col)

def print_board(board):         #defines function to display board
    for line in board:
        print (" ".join(line))

print ("Alrighty, that be the ocean, where be me ships then matey?")
print_board(board)              #dispays board

class battleships(object):
    def __init__(self, ship_name):
           self.ship_name = ship_name

def ship_square(ship):                              #defines function to generate ship square locations
        ship_row = randint(1, board_row)
        ship_col = randint(1, board_col)
        return (ship_row, ship_col)

def check_location(this_ship, shipA, shipB, shipC):         #defines function to check ships do not overlap
    while ship_square(this_ship) == ship_square(shipA) or ship_square(this_ship) == ship_square(shipB) or ship_square(this_ship) == ship_square(shipC):
        ship_square(this_ship)
    return ship_square(this_ship)
           
    
ship1 = battleships("The Black Pearl")          #creates battleships as instances of battleships class
ship2 = battleships("The Inferno")   
ship3 = battleships("Jolly Roger")                  #ALL 1 SQUARE BATTLESHIPS FOR NOW!!!
ship4 = battleships("The Walrus")


ship_square1 = ship_square(ship1)                      #runs functions to generate ship square locations and check for overlaps
ship_square(ship2)                                     #saves ship square locations as values for comparisons
ship_square2 = check_location(ship2, ship1, ship1, ship1 ) 
ship_square(ship3)
ship_square3 = check_location(ship3, ship1, ship2, ship1)
ship_square(ship4)
ship_square4 = check_location(ship4, ship1, ship2, ship3)


guess = 1    



def check_guess():
    if guess_ship_square == ship_square1:
        print ("Argh there she goes,", ship1.ship_name,"! A fine ship she war... Not bad,", user,"!")
        board[(guess_row - 1)][(guess_col - 1)] = "*"
    elif guess_ship_square == ship_square2:
        print ("Argh there she goes,", ship2.ship_name,"! A fine ship she war... Not bad,", user,"!")
        board[(guess_row - 1)][(guess_col - 1)] = "*"
    elif guess_ship_square == ship_square3:
        print ("Argh there she goes,", ship3.ship_name,"! A fine ship she war... Not bad,", user,"!")
        board[(guess_row - 1)][(guess_col - 1)] = "*"
    elif guess_ship_square == ship_square4:
        print ("Argh there she goes,", ship4.ship_name,"! A fine ship she war... Not bad,", user,"!")
        board[(guess_row - 1)][(guess_col - 1)] = "*"

    elif guess_row < 1 or guess_row > board_row or guess_col < 1 or guess_col > board_col:              #NEEDS FIX!!!
        print ("Try firing at the water!")
    elif board[(guess_row -1)] == "X" or board[(guess_col-1)] == "X":
        print ("What's the matter, matey, ye lost yer mind? Ye just shot thur.")
    else:
        print ("Bad shot, matey!")
        board[(guess_row - 1)][(guess_col - 1)] = "X"
    global guess
    guess += 1

    if guess == 10:
        print ("Game Over")

    print ("Turns left: ",(guess))
    print_board(board)   

while guess <= 10:
    
    
    guess_row = input("Which row? ")
    guess_row = int(guess_row)
    guess_col = input("Ha! Which column? ")
    guess_col = int(guess_col)
    guess_ship_square = (guess_row, guess_col)

    check_guess()

           


