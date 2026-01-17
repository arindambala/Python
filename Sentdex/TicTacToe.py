'''

# Program to demonstarte a tic-tac-toe game - Sentdex | YouTube.
# This code is released on a personal computer.
# (c) 2026, Arindam Bala.

''' 

import itertools

# ----_---- VICTORY CHECK ----_----
def victory(matx):
    
    def all_cases(ll):
        if ll.count(ll[0]) == len(ll) and ll[0] != 0:
            return True
        else:
            return False
    
    # Rows
    for row in matx:
        print(row)
        if all_cases(row):
            print(f"\nVictory! Player {row[0]} horizontally (=)!")
            return True

    # Diagonals
    diags = []
    for col, row in enumerate(reversed(range(len(matx)))):
        diags.append(matx[row][col])
    if all_cases(diags):
            print(f"\nVictory! Player {diags[0]} diagonally! (//)")
            return True

    
    diags = []
    for idx in range(len(matx)):
        diags.append(matx[idx][idx])
    if all_cases(diags):
            print(f"\nVictory! Player {diags[0]} diagonally! (\\)")
            return True

    # Columns
    for col in range(len(matx)):
        check = []
        for row in matx:
            check.append(row[col])
        if all_cases(check):
            print(f"\nVictory! Player {check[0]} vertically (||)!")
            return True
    
    return False

# Functions
def matx_board(matx_map, player=0, row=0, column=0, just_display=False): # Avoids repetition - DRY (Don't Repeat Yourself)
    try:
        if matx_map[row][column] != 0:
            print("Position already occupied! Choose another space!")
            return matx_map, False
        print("\n   "+"  ".join(chr(ord('a') + i) for i in range(len(matx_map))))# print ("   a  b  c")
        if not just_display:
            matx_map[row][column] = player
        for i, row in enumerate(matx_map):
            print (chr(ord('a') + i), row)
        return matx_map, True
    except IndexError as err:
        print("ERROR: Did you give row/column > 2? ", err)
        return matx_map, False
    
    except Exception as err:
        print("Error: Something went wrong!:( ", err)
        return matx_map, False

'''matx_board() # call = matx_board

matx[0][1] = 1
matx_board() # call()'''

turn = True
players = [1, 2]

while turn:
    matx_size =int(input("\nWhat size of TicTacToe do you want to play? (Think): "))
    matx = [[0 for i in range(matx_size)] for i in range(matx_size)]

    won = False
    matx, _ = matx_board(matx, just_display=True)
    play_choice = itertools.cycle(players)
    while not won:
        curr_player = next(play_choice)
        print(f"\nCurrent Player: {curr_player}")
        turn_over = False
        
        while not turn_over:
            row_choice = int(input("What row you want to play? : "))
            col_choice = int(input("What column do you want to play? : "))
            matx, turn_over = matx_board(matx, curr_player, row_choice, col_choice)
        
        if victory(matx):
            won = True
            while True:
                replay = input("\nGame's over. Would you like to play agian? (y/n): ")
                if replay.lower() == 'y':
                    print("Here we go again....!!!")
                    break
                elif replay.lower() == 'n':
                    print("Understandable. Have a nice day....!!!")
                    turn = False
                    break
                else:
                    print("Are you serious mah brutha....???")


''' import itertools # REFACTORED

# ---------------- Victory Check ----------------
def victory(matx):
    def all_cases(ll):
        return ll.count(ll[0]) == len(ll) and ll[0] != 0

    # Rows
    for row in matx:
        if all_cases(row):
            print(f"\nVictory! Player {row[0]} horizontally (=)!")
            return True

    # Diagonal \
    if all_cases([matx[i][i] for i in range(len(matx))]):
        print(f"\nVictory! Player {matx[0][0]} diagonally (\\)!")
        return True

    # Diagonal //
    if all_cases([matx[i][len(matx) - i - 1] for i in range(len(matx))]):
        print(f"\nVictory! Player {matx[0][-1]} diagonally (//)!")
        return True

    # Columns
    for col in range(len(matx)):
        if all_cases([row[col] for row in matx]):
            print(f"\nVictory! Player {matx[0][col]} vertically (||)!")
            return True

    return False


# ---------------- Board Display ----------------
def print_board(matx):
    size = len(matx)
    print("\n   " + "  ".join(chr(ord('a') + i) for i in range(size)))
    for i, row in enumerate(matx):
        print(chr(ord('a') + i), row)


# ---------------- Make Move ----------------
def make_move(matx, player, row, col):
    try:
        if matx[row][col] != 0:
            print("Position already occupied! Try again.")
            return False
        matx[row][col] = player
        return True
    except IndexError:
        print("Invalid position! Out of bounds.")
        return False


# ---------------- Game Loop ----------------
turn = True
players = [1, 2]

while turn:
    size = int(input("\nWhat size TicTacToe board? : "))
    matx = [[0 for _ in range(size)] for _ in range(size)]

    won = False
    play_choice = itertools.cycle(players)

    print_board(matx)  # show initial empty board once

    while not won:
        curr_player = next(play_choice)

        print("\n" + "-" * 30)
        print(f"Current Player: {curr_player}")

        turn_over = False
        while not turn_over:
            row_choice = int(input("Row: "))
            col_choice = int(input("Column: "))
            turn_over = make_move(matx, curr_player, row_choice, col_choice)

        print_board(matx)  # show board ONCE after move

        if victory(matx):
            replay = input("\nGame over. Play again? (y/n): ")
            if replay.lower() != 'y':
                turn = False
            break '''