import time

def starting_gameboard():
    table = [[" "," "," "], [" "," "," "], [" "," "," "]]
    return table

def instructions():
    print("Let's play a game of tic tac toe.")
    time.sleep(2)
    print("Player 1 is always X and Player 2 is always O.")
    time.sleep(2)
    print("The top left square is 1 and the bottom right square is 9.")
    time.sleep(2)
    print("Example: if you are playing X, its your turn, and the bottom left square is open, say 7")

def tic_tac_toe():
    board = starting_gameboard()
    player = True #True for X, False for Y
    player_num = 1
    turn = 0
    win = False
    pos = 0
    while win != True:
        print(board[0])
        print(board[1])
        print(board[2])
        pos = input(f"You are player {player_num}. Where would you like to play?\n")
        pos = int(pos) - 1
        row = pos // 3
        col = pos % 3
        print("Calculating...")
        time.sleep(0.5)
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
                board[row][col] = "Y"
                player = not player
                player_num = 1
                turn += 1
        if turn == 9:
            print("This is a tied game.")
            win = "Draw"
    print("You have drawn this game. Thank you for playing.")

def win_check():
    winning_combos = [[0,0],[1,1],[2,2]],[[0,0],[1,0],[2,0]],[[0,0],[0,1],[0,2]],[[2,0],[2,1],[2,2]],[[1,0],[1,1],[1,2]],[[2,0],[1,1],[0,2]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]]


#Make a win condition that loop through every win combo.

#instructions()
tic_tac_toe()
