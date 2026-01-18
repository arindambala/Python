'''

# Program to demonstarte a game of noughts & crosses - Sentdex | YouTube.
# This code is released on a personal computer.
# (c) 2026, Arindam Bala.

'''

import itertools
from colorama import Fore, Style, init

init()

# ---------------- Display ----------------
# PLAYER_SYMBOLS = {
#     0: ' ', # Empty
#     1: Fore.MAGENTA + 'X' + Style.RESET_ALL,
#     2: Fore.CYAN + 'O' + Style.RESET_ALL
# }

# ---------------- Victory Check ----------------
def victory(board):
    def all_cases(ll):
        return ll.count(ll[0]) == len(ll) and ll[0] != 0
    
    # Rows
    for row in board:
        if all_cases(row):
            print(f"\nVICTORY! Player {row[0]} HORIZONTALLY (=)!")
            return True
    
    # Diagonals
    if all_cases([board[i][i] for i in range(len(board))]):
        print(f"\nVICTORY! Player {board[0][0]} DIAGONALLY (\\)!")
        return True
    
    if all_cases([board[i][len(board) - i - 1] for i in range(len(board))]):
        print(f"\nVICTORY! Player {board[0][-1]} DIAGONALLY (//)!")
        return True

    # Columns
    for col in range(len(board)):
        if all_cases([row[col] for row in board]):
            print(f"\nVICTORY! Player {board[0][col]} VERTICALLY (||)!")
            return True

    return False

# ---------------- Draw Check ----------------
def draw(board):
    for row in board:
        if 0 in row:
            return False
    return True

# ---------------- Board Display ----------------
def print_board(board):
    size = len(board)
    print("\n   " + "  ".join(chr(ord('a') + i) for i in range(size)))
    for i, row in enumerate(board):
        color_row = ""
        for item in row:
            if item == 0:
                color_row += "   "
            elif item == 1:
                color_row += Fore.MAGENTA + ' X ' + Style.RESET_ALL
            elif item == 2:
                color_row += Fore.CYAN + ' O ' + Style.RESET_ALL
        print(chr(ord('a') + i), color_row)

# ---------------- Update Move ----------------
def update_move(board, player, row, col):
    try:
        if board[row][col] != 0:
            print("\nPosition already occupied! Allow that! Try again innit.\n")
            return False
        board[row][col] = player
        return True
    except IndexError:
        print("\nINVALID! Out of bounds & allat.\n")
        return False

# ---------------- Turn Choice ----------------
turn = True
players = [1, 2]

while turn:
    size = int(input("\nWhat's the board size fam? : "))
    board = [[0 for _ in range(size)] for _ in range(size)]
    
    won = False
    player_turn = itertools.cycle(players)
    
    print_board(board) # Initial empty board
    
    while not won:
        curr_player = next(player_turn)
        
        print("\n" + "-" * 30)
        print(f"Current Player: {curr_player}")
        
        turn_over = False
        while not turn_over:
            row_choice = int(input("Row: "))
            col_choice = int(input("Column: "))
            turn_over = update_move(board, curr_player, row_choice, col_choice)
            print("-" * 30)
        
        print_board(board) # Updated board
        
        if victory(board):
            won = True
            while won:
                replay = input("\nGame concluded. Reload the ting? (y/n): ")
                if replay.lower() == 'y':
                    print("\nOi, man's actually got sense.")
                    break
                elif replay.lower() == 'n':
                    print("\nIght bet. Fair play my g.")
                    turn = False
                    break
                else:
                    print(f"\nAre you mad bruv!?")
        
        elif draw(board):
            print(f"\nDRAW! Game's gone! It can't go on like this?! Can it?!")
            won = True
            while won:
                replay = input("\nDon't take the mick now lah! (y/n): ")
                if replay.lower() == 'y':
                    print("\nOi, man's actually got sense.")
                    break
                elif replay.lower() == 'n':
                    print("\nIght bet. Fair play my g.")
                    turn = False
                    break
                else:
                    print(f"\nAre you mad bruv!?")