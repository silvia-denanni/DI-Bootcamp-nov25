# MINI PROJECT 1

#1)LIST OF LISTS TO REPRESENT VISUALLY THE BOARD, each grid cell should be empty " "

#2)def display_board(): a function to visually represent the 3x3 grid , FORMAT THE OUTPUT CLEARLY

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

print("*"*15)                                             

def display_board(board):    
    for column, row in enumerate(board):
        print(f"*{row[0]}  |  {row[1]}  |  {row[2]}*")
        if column < 2:                                        #checks if the current row is not the last row
                print("*---+-----+---*")

display_board(board)
print("*"*15) 

#3)Getting Player Input    

def player_input(player):    
    while True:
        player_row = int(input("Enter row between 0-2"))
        player_column = int(input("Enter column between 0-2"))
        
        if player_row < 0 or player_row > 2 or player_column < 0 or player_column > 2: 
            print("Try again! You are out of bounds.")
            continue
        if board[player_row][player_column] != " ":
            print("Try again! The cell is occupied.")
            continue
        board[player_row][player_column] = player
        break     
#return player_row, player_column

#4) Checking for a Winner

def check_win(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
        
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False 

#5) Checking for a Tie

def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True

#6) The Main Game Loop        

def play():            #Reset the board at the start of the game
    for i in range(3):
        for j in range(3):
            board[i][j] = " "
    
    current_player = "X"  # X always starts
    while True:
        display_board(board)

        player_input(current_player)

        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins! Congratulations!")
            break
        
        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break
        
        # Switch player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

# Start the game
play()

