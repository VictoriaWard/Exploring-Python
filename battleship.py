# battleship.py
# by Victoria Ward
# A simple version of the classic battleship game
# Set your difficulty level by choosing board size

from random import randint      #imports randint function to help to generate battleships

user = input("Welome to Battleship, Pirate! What do we call ye? ")       #gets user name
print ("\nAlright", user, "matey... let's see what yer got! ")          #starts game

board_col = input("\nHow big's the ocean, how many columns be she? (minimum 4) ")      #gets board size, columns
board_col = int(board_col)                  #converts to int for calculations
board_row = input("\nAnd how many rows be she? (minimum 4) ")          #gets board size, rows
board_row = int(board_row)                  #converts to int for calculations

board_size = board_row * board_col          #calculates board size
if board_size <= 20:                        #comments on chosen difficulty level
    print ("\nHa ha ha! Not so tough ey matey!") 
if 21 <= board_size <= 36:
    print ("\nThink ye tough ey matey!")
if 37 <= board_size <= 49:
    print ("\nYou know somethin' I don't, hotshot?")
if board_size >= 50:
    print ("\nCrikey! He's a madman!")

board = []                      #creates board            
for x in range(1, board_row + 1):                
    board.append(["O"] * board_col)

def print_board(board):         #defines function to display board
    for line in board:
        print (" ".join(line))

print ("\nAlrighty, that be the ocean, where be me ships then matey?")
print_board(board)              #dispays board

class battleships(object):                          #NEED CLASS???
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


guess = 1                               #assigns value of 1 to guess variable. player is allowed 10 guesses
hit1 = False                            #creates variables to record if ships have been hit
hit2 = False
hit3 = False
hit4 = False


def check_guess():                      #defines fuction to check guess location against ship locations
    if guess_row < 1 or guess_row > board_row or guess_col < 1 or guess_col > board_col:      #checks that player guesses within board limits       
        print ("\nTry firing at the water!")
    elif board[(guess_row -1)][(guess_col-1)] == "X" or board[(guess_row -1)][(guess_col-1)] == "*":         #checks that player has not already guessed here                  
        print ("\nWhat's the matter, matey, ye lost yer mind? Ye just shot thur.")
        
    elif guess_ship_square == ship_square1:                       #checks for a correct guess
        print ("\nArgh there she goes,", ship1.ship_name,"! A fine ship she war... Not bad,", user,"!")
        board[(guess_row - 1)][(guess_col - 1)] = "*"       #updates board to display hit battleship
        global hit1                                          #declares hit variables as global variables
        hit1 = True
                                                
    elif guess_ship_square == ship_square2:
        print ("\nArgh there she goes,", ship2.ship_name,"! A fine ship she war... Not bad,", user,"!")
        board[(guess_row - 1)][(guess_col - 1)] = "*"
        global hit2
        hit2 = True
        
    elif guess_ship_square == ship_square3:
        print ("\nArgh there she goes,", ship3.ship_name,"! A fine ship she war... Not bad,", user,"!")
        board[(guess_row - 1)][(guess_col - 1)] = "*"
        global hit3
        hit3 = True
        
    elif guess_ship_square == ship_square4:
        print ("\nArgh there she goes,", ship4.ship_name,"! A fine ship she war... Not bad,", user,"!")
        board[(guess_row - 1)][(guess_col - 1)] = "*"
        global hit4
        hit4 = True
        
            

    else:
        print ("\nBad shot, matey!")                        #dispays miss message if player fails to hit battleship
        board[(guess_row - 1)][(guess_col - 1)] = "X"       #updates board to display guessed square
        
    global guess                                            #declares guess variable as global to override local behaviour
    guess += 1                                              #updates number of guesses

    if guess > 10:                                          #dispays game over message if player has had ten guesses
        print ("\nGAME OVER!")

    if guess <= 10:
        print ("\nShots left: ",(10 - guess))               #displays number of remaining guesses                                       
        print_board(board)                                  #dispays updated board

while guess <= 10:                                          #continues game up to ten guesses
    
    guess_row = input("\nWhich row? ")                      #gets player's row guess
    if str.isdigit(guess_row) == False:                         #checks that player has enter a number 
        guess_row = input("\Argh, what e sayin'? Which row I say?")
    guess_row = int(guess_row)                              #converts guess to int for comparisons
    guess_col = input("\nHa! Which column? ")               #gets player's column guess
    if str.isdigit(guess_col) == False:
        guess_col = input("\Argh, what e sayin'? Which column I say?")
    guess_col = int(guess_col)                              #converts guess to int for comparisons
    guess_ship_square = (guess_row, guess_col)              #stores guesses in one value
                                                            
    check_guess()                                           #runs check guess function to check guess location against ship locations and update board

    if hit1 == hit2 == hit3 == hit4 == True:                #checks if player has won and ends game
        print ("\nSHIVER ME TIMBERS! YE DONE IT!")
        break


