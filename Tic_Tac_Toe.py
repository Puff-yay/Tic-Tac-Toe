import time

def starting_gameboard():
    table = [[" "," "," "], [" "," "," "], [" "," "," "]]
    return table

def instructions():
    print("Take turns entering a number (1-9) to place your mark on the grid. The first player to get three in a row wins!")
    time.sleep(2)
    print("Player 1 is always X and Player 2 is always O.")
    time.sleep(2)
    print("The top left square is 1 and the bottom right square is 9.")
    time.sleep(2)
    print("Example: If you want to play in the center AND the center is open AND it's your turn, say 5.")

def tic_tac_toe():
    board = starting_gameboard()
    player = True #True for X, False for O
    player_num = 1
    turn = 0
    pos = 0
    while turn < 9:
        print(board[0])
        print(board[1])
        print(board[2])
        if board[0][0] == board[0][1] == board[0][2] and board[0][0] != " ": #Top Row
            print("We have a winner.")
            if board[0][0] == "X":
                print("Player 1 has won.")
                return
            else:
                print("Player 2 has won.")
                return
        if board[1][0] == board[1][1] == board[1][2] and board[1][0] != " ": #Center Row
            print("We have a winner.")
            if board[1][0] == "X":
                print("Player 1 has won.")
                return
            else:
                print("Player 2 has won.")
                return
        if board[2][0] == board[2][1] == board[2][2] and board[2][0] != " ": #Bottom Row
            print("We have a winner.")
            if board[2][0] == "X":
                print("Player 1 has won.")
                return
            else:
                print("Player 2 has won.")
                return
        if board[0][0] == board[1][0] == board[2][0] and board[0][0] != " ": #Left Column
            print("We have a winner.")
            if board[0][0] == "X":
                print("Player 1 has won.")
                return
            else:
                print("Player 2 has won.")
                return
        if board[0][1] == board[1][1] == board[2][1] and board[0][1] != " ": #Middle Column
            print("We have a winner.")
            if board[0][1] == "X":
                print("Player 1 has won.")
                return
            else:
                print("Player 2 has won.")
                return
        if board[0][2] == board[1][2] == board[2][2] and board[0][2] != " ": #Right Column
            print("We have a winner.")
            if board[0][2] == "X":
                print("Player 1 has won.")
                return
            else:
                print("Player 2 has won.")
                return
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ": #Top Left to Bottom Right Diagonal
            print("We have a winner.")
            if board[0][0] == "X":
                print("Player 1 has won.")
                return
            else:
                print("Player 2 has won.")
                return
        if board[2][0] == board[1][1] == board[0][2] and board[2][0] != " ":
            print("We have a winner.")
            if board[2][0] == "X":
                print("Player 1 has won.")
                return
            else:
                print("Player 2 has won.")
                return
        pos = input(f"You are player {player_num}. Where would you like to play?\n")
        pos = int(pos) - 1
        row = pos // 3
        col = pos % 3
        if pos < 0 or pos > 9:
            print("Please pick another square")
            continue
        elif board[row][col] != " ":
            print("This square is occupied!")
            time.sleep(1)
            print("Please pick another square")
        else:
            if player:
                board[row][col] = "X"
                player = not player
                player_num = 2
                turn += 1
            else:
                board[row][col] = "O"
                player = not player
                player_num = 1
                turn += 1
    print("This is a tied game.")
    return

#instructions()
tic_tac_toe()
