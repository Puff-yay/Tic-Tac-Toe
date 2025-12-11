import time

def starting_gameboard():
    table = [[1,2,3], [4,5,6], [7,8,9]]
    return table

def position_converter_set_a(position):
    column = position % 3
    return column

def position_converter_set_b(position):
    row_num = (position // 3) - 1
    return row_num

def instructions():
    print("Let's play a game of tic tac toe.")
    time.sleep(2)
    print("Player 1 is always X and Player 2 is always O.")
    time.sleep(2)
    print("Say the number you want your X or O to go in.")
    time.sleep(2)
    print("Example: if you are playing X, its your turn, and the bottom left square is open, say 7")

def tic_tac_toe():
    board = starting_gameboard()
    player_num = 1
    print(board[0])
    print(board[1])
    print(board[2])
    [[0,0],[1,1],[2,2]]
    # #1 set is upper left to bottom right diagonal.

    win = False
    while win != True:
        position = input(f"You are player {player_num}. Where would you like to play?\n")
        if board[position_converter_set_a(int(position))][position_converter_set_b(int(position))] not in ["X","Y"] and player_num == 1: #board[0][0] etc.
            board[position_converter_set_a(int(position))][position_converter_set_b(int(position))] = "X"
            player_num = 2
        elif board[position_converter_set_a(int(position))][position_converter_set_b(int(position))] not in ["X","Y"] and player_num == 2:
            board[position_converter_set_a(int(position))][position_converter_set_b(int(position))] = "Y"
            player_num = 1
        else:
            print("That is not an open spot. Pick another one.")
            time.sleep(1)

#Need to add a while loop that tracks if the position of the board isn't in a winnning condition, continue the game.
#Also need to add a condition where if a game is a tie, it proclaims a tie.


#instructions()
tic_tac_toe()