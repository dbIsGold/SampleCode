
# This is a game of Tic-Tac-Toe Played against the Computer
# The Human Player uses the symbol X and the computer uses O. For extra clarity each of these symbols are colored coded
# who ever gets consecutive 3 symbols in spots next to ech other horizontally, vertically or diagonally, wins!

# Usage: python ./TicTacToe.py
# ------------------------------------

import random
import os
from copy import deepcopy

# Declares constant
COMPUTER = 'O'
HUMAN = 'X'
COLSYM = ' | '
ROWSYM = '-'
TOTSPOT = 9
MAXCOL = 3
RED = '\033[91m'
BLUE = '\033[94m'
BOLD     = '\33[1m'
UNDERLINE = '\33[4m'
ENDCODE = '\033[0m'

def clean_slate():
    # Clear the screen
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def draw_slate(mat):
    # Clear the screen and redraw the current game with pipe separating columns and hyphen separating row.
    # Format the messages with extra formatting
    clean_slate()
    print(BOLD + UNDERLINE + "This is a game of Tic-Tac-Toe where You play against the computer" + ENDCODE)
    print("The Computer selects a position randomly.\n")
    print("You are "+ BLUE + BOLD + "X" + ENDCODE +" and the Computer is " + RED + BOLD+ "O\n" + ENDCODE)
    
    # We want the X to be printed in blue color and the O in red
    # But we don't want to change the original values in the list because it will effect it's comparison functionality
    # Hence we are making a deep copy of the game mat and changing only the copy with color codes
    color_mat = deepcopy(mat)
    # Color code the X and O
    for i in range(MAXCOL):
        for j in range(MAXCOL):
            if color_mat[i][j] == HUMAN:
                color_mat[i][j] = BLUE + HUMAN + ENDCODE
            elif color_mat[i][j] == COMPUTER:
                color_mat[i][j] = RED + COMPUTER + ENDCODE

    # Print the colored game mat
    i = 0    
    for row in color_mat:
        i += 1
        print("\t" + COLSYM.join(row))
        if i < len(color_mat):
            print("\t" + ROWSYM * TOTSPOT)


def check_game_over(mat):
    # Check if every spot on the game mat has been filled. 
    # Returns True if all spots are filled and indicates that the game is over
    
    return all(col != " " for line in mat for col in line)

def make_a_play(mat, player):
    # This function lets the player choose a spot on game mat and places an X
    # OR generates a random move for the computer to place a O
    # If the spot is already occupied or out of range, an error message is generated
    while True:
        try:
            if player == COMPUTER:
                spot = (random.randint(1, TOTSPOT) - 1 ) 
            else: 
                spot = int(input(f"\nPlease enter your move (1-9): ")) - 1
            i, j =  divmod(spot, MAXCOL)
            if 0 <= spot <= TOTSPOT - 1 and mat[i][j] == " ":
                mat[i][j] = player
                return
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 9.")

def check_game_winner(mat, player):
    # Check all the winning combinations 
    
    # 1. Horizontal 
    for i in mat:
        if all(j == player for j in i):
            return True
    # 2. Vertical 
    for j in range(MAXCOL):
        if all(mat[i][j] == player for i in range(MAXCOL)):
            return True
    # 3. Diagonal 
    if all(mat[i][i] == player for i in range(MAXCOL)) or all(mat[i][2 - i] == player for i in range(MAXCOL)):
        return True   
    return False

def get_next_player(cur_player):
    # Get the next player based on the current player
    if cur_player == COMPUTER:
        next_player = HUMAN
    else:
        next_player = COMPUTER
    return next_player

def match():
    # Creates a 3 x 3 game mat and plays the game
    # Randomly generates a spot for COMPUTER
    # Accepts a spot from user 
    # Checks if a winner can be declared in the game.
    mat = [[" " for _ in range(MAXCOL)] for _ in range(MAXCOL)]
    player = HUMAN
    while True:
        draw_slate(mat)
        make_a_play(mat, player)
        if check_game_winner(mat, player):
            draw_slate(mat)
            if player == HUMAN:
                dec_winner = "Congrats!! YOU WIN THE GAME AGAINST THE COMPUTER!!"
            else:
                dec_winner = "Sorry you lost!! THE COMPUTER WINS THE GAME!!"
            print("\n" + dec_winner + "\n")
            break
        if check_game_over(mat):
            draw_slate(mat)
            print("\nYou Tied the game with the Computer!!\n")
            break

        player = get_next_player(player)
                  

if __name__ == "__main__":
    match()
