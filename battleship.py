from random import randint
''' Battleship implementation - does not have to be a square board '''

board = [] # displayed board
ships = [] # board with ships are located
types = {} # types of ships and size
nrows = 10 # number of rows on board
ncols = 10 # number of columns on board

# Create board for other player and for ships
for x in range(nrows):
    board.append(["O"] * ncols)
    ships.append(["O"] * ncols)

# Define type of ships : sizes and position them
types = {
    "carrier": 5,
    "battleship": 4,
    "cruiser": 3,
    "submarine": 3,
    "destroyer": 2
}
    
def print_board(board):
    col = 0
    temp = []
    print " ", 
    for i in range(nrows):
        print i, 
    print ""
    for row in board:
        print col, " ".join(row)
        col += 1

# gives random position based on ship size
def random_pos(size):
    return randint(0, nrows-size-1)

# check if position is valid
def isValid(row, col, size, orientation):
    valid = True
    if orientation:
	for i in range(size):
	    valid = valid and (row+i) in range(0, nrows) and col in range(0, ncols) and ships[row+i][col] == "O"
    else:
	for i in range(size):
	    valid = valid and row in range(0, nrows) and (col+i) in range(0, ncols) and ships[row][col+i] == "O"
    return valid;

# place ship
def place(ship):
    size = types[ship]

    # assign dummy values for isValid()
    x = y = orientation = -1
    
    while not isValid(x, y, size, orientation):
        orientation = randint(0,1)
        if orientation:
            x = random_pos(size)
	    y = random_pos(1)
	else:
            x = random_pos(1)
	    y = random_pos(size)

    for i in range(size):
        if orientation:
	    ships[x+i][y] = "X"
        else:
	    ships[x][y+i] = "X"
    # Test
    # print ship, size, x, y

for type in types:
    place(type)
#print_board(ships)

# Game implementation
print "Let's play Battleship!"
print_board(board)
win = False # Cannot win at the beginning of the game.

#nturns = 20 # If want to limit game to a certain number of turns
#for turn in range(nturns):
turn = 0

# Play until you win
while not win:
    print "Turn ", turn+1
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))

    if (guess_row not in range(nrows)) or (guess_col not in range(ncols)):
        print "Oops, that's not even in the ocean."
    elif(board[guess_row][guess_col] != "O"):
        print "You guessed that one already."   
    elif ships[guess_row][guess_col] == "X":
	print "Hit!"
	ships[guess_row][guess_col] = "H"
        board[guess_row][guess_col] = "H"
        win = True # Assume it was the last hit, but check if there are any other x's
        for i in range(len(ships)):
	    win = win and not ('X' in ships[i])
        if win:
	    print "Congratulations! You sunk my battleship!"
            print_board(ships)
    else:
        print "You missed!"
        board[guess_row][guess_col] = "X"
       
    print_board(board)
    turn += 1
    
