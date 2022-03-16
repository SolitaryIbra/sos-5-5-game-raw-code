# -Name: Ibrahim Tarek Ibrahim Mohamed
# -Student_ID: 20211002
# -Course: Structured Programming _CS112_
# -This code is directed to Dr. Mohamed EL-Ramly 
# and CANNOT be shared except by the owner's permission
# -Game: S-O-S game: (5x5)
#######################################################

og_board = [[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4]]
pl_1, pl_2 = [],[]      # lists to save the value of points of each player


## Display the board (5x5)
def display_status():

    # Loop to show the board
    for row in og_board:
        print(row)


## Get row input From User
def get_row(player):

    # Input the Row
    while True:
        try:
            message_row = f"player {player}, Enter row from (0 to 4): "
            input_row= int(input(message_row))
            if input_row in range(len(og_board)):       # check if input row out of range
                break
        except BaseException:
            pass

    return input_row        # save the value of the row


## Get column input From User
def get_column(player,input_row):

    # Input the column
    while True:
        try:
            message_column= f"player {player}, Enter column from (0 to 4): "
            input_column = int(input(message_column))
            if input_column in range(len(og_board[input_row])):     # check if input column is not used
                break
        except BaseException:
            pass

    return input_column     # save the value of column


## Check if the coordinates is already used
def used_coordinates(row,column):

    # check if the coordinates(row/column) are already used
    if og_board[row][column] == "s" or og_board[row][column] == "o":
        return "used"


## Get s/o from user
def get_s_o(player):

    # Input s/o
    while True:
        try:
            message_s_o = f"player {player}, Enter either -s- or -o- "
            input_s_o = input(message_s_o).lower().strip()
            if input_s_o == "s" or input_s_o == "o":
                break
        except BaseException:
            pass

    # save the input either(s/o)        
    return input_s_o


## Combine the inputed row and column in one list
def format_list(input_row,input_column,input_s_o):

    # assign the coordinates and saved s/o in one list
    player_input = [input_row, input_column,input_s_o]

    # save the list 
    return player_input


## Update Board
def update_board(player_input):
    og_board[player_input[0]][player_input[1]] = player_input[-1]


## Winning Possibilities, p_i is player_input
def points_situation(inp):
    points = 0
    try:
        if [og_board[inp[0]][inp[1]-1] , og_board[inp[0]][inp[1]], og_board[inp[0]][inp[1]-1]] == ["s","o","s"]:
            points += 1
    except BaseException:
        pass

    try:
        if [og_board[inp[0]][inp[1]+2] , og_board[inp[0]][inp[1]+1], og_board[inp[0]][inp[1]]] == ["s","o","s"]:
            points += 1
    except BaseException:
        pass

    try:
        if [og_board[inp[0]][inp[1]-2] , og_board[inp[0]][inp[1]-1], og_board[inp[0]][inp[1]]] == ["s","o","s"]:
            points += 1
    except BaseException:
        pass

    try:
        if [og_board[inp[0]-2][inp[1]] , og_board[inp[0]-1][inp[1]], og_board[inp[0]][inp[1]]] == ["s","o","s"]:
            points += 1
    except BaseException:
        pass

    try:
        if [og_board[inp[0]+2][inp[1]] , og_board[inp[0]+1][inp[1]], og_board[inp[0]][inp[1]]] == ["s","o","s"]:
            points += 1
    except BaseException:
        pass

    try:
        if [og_board[inp[0]-1][inp[1]] , og_board[inp[0]][inp[1]], og_board[inp[0]+1][inp[1]]] == ["s","o","s"]:
            points += 1
    except BaseException:
        pass

    try:
        if [og_board[inp[0]+1][inp[1]-1] , og_board[inp[0]][inp[1]], og_board[inp[0]-1][inp[1]+1]] == ["s","o","s"]:
            points += 1
    except BaseException:
        pass

    try:
        if [og_board[inp[0]+2][inp[1]-2] , og_board[inp[0]+1][inp[1]-1], og_board[inp[0]][inp[1]]] == ["s","o","s"]:
            points += 1
    except BaseException:
        pass

    try:
        if [og_board[inp[0]][inp[1]] , og_board[inp[0]-1][inp[1]+1], og_board[inp[0]-2][inp[1]+2]] == ["s","o","s"]:
            points += 1
    except BaseException:
        pass

    try:
        if [og_board[inp[0]-1][inp[1]-1] , og_board[inp[0]][inp[1]], og_board[inp[0]+1][inp[1]+1]] == ["s","o","s"]:
            points += 1
    except BaseException:
        pass

    try:
        if [og_board[inp[0]-2][inp[1]-2] , og_board[inp[0]-1][inp[1]-1], og_board[inp[0]][inp[1]]] == ["s","o","s"]:
            points += 1
    except BaseException:
        pass

    try:
        if [og_board[inp[0]][inp[1]] , og_board[inp[0]+1][inp[1]+1], og_board[inp[0]+2][inp[1]+2]] == ["s","o","s"]:
            points += 1
    except BaseException:
        pass
    
    return (points)


## Finishing the Game
def finish_game():
    
    # loop to see if an integer is still in the board
    active = True
    for row in og_board:
        for column in row:
            if column in [0,1,2,3,4]:       # if integer excists, break the finish game loop
                active = False
                break

    if active == True:      # if there is no integer left, end the game and assign the winner or draw
        if sum(pl_1) > sum(pl_2):
            return "p1"
        elif sum(pl_1) < sum(pl_2):
            return "p2"
        elif sum(pl_1) == sum(pl_2):
            return "draw"


## Play Game
def game_main():
    while True:

        # Player One
        display_status()        # Show the board

        active = True       
        while active:       # start the loop for taking the input
            row = get_row("One")        # input row
            column = get_column("One",row)      # input column
            if used_coordinates(row,column) != "used":      # check if the coordinates are used or not
                active = False      # if not used, break the inner loop
            else:
                print(f"Player One, please enter an unused coordinate.")

        s_o = get_s_o("One")        # input s/o
        list_input = format_list(row,column,s_o)        # adding the row, column, input s/o in a list variable
        update_board(list_input)        # update the board ny the inputted coordinates and s/o
        pl_1_points = points_situation(list_input)      # checking points cases
        pl_1.append(pl_1_points)        # adding points to player one score

        # checking if the game has finished. If finished, break the main loop
        check_game_end = finish_game()      
        if check_game_end == "p1":
            print("Player One Wins")
            break
        elif check_game_end == "p2":
            print("Player Two Wins")
            break
        elif check_game_end == "draw":
            print("The Game is draw")
            break
        else:
            pass
        
###
###
###

        # Player Two
        display_status()        # Show the board

        active = True
        while active:       # start the loop for taking the input
            row = get_row("Two")        # input row
            column = get_column("Two",row)      # input column
            if used_coordinates(row,column) != "used":      # check if the coordinates are used or not
                active = False      # if not used, break the inner loop
            else:
                print(f"Player Two, please enter an unused coordinate.")               
        s_o = get_s_o("Two")        # input s/o
        list_input = format_list(row,column,s_o)        # adding the row, column, input s/o in a list variable
        update_board(list_input)        # update the board ny the inputted coordinates and s/o
        pl_2_points = points_situation(list_input)      # checking points cases
        pl_2.append(pl_2_points)        # adding points to player one score



game_main()
