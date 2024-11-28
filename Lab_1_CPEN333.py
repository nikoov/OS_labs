# student name: Nikoo Vali
# student number: 83343012

# A command-line Tic-Tac-Toe game 
import random

board = [' '] * 9 # A list of 9 strings, one for each cell, 
                  # will contain ' ' or 'X' or 'O'
played = set()    # A set to keep track of the played cells 

def init() -> None:
    """ prints the banner messages 
        and prints the intial board on the screen
    """
    print("Welcome to Tic-Tac-Toe!")
    print("You play X (first move) and computer plays O.")
    print("Computer plays randomly, not strategically.")
    printBoard()

def printBoard() -> None:
    """ prints the board on the screen based on the values in the board list """
    #To Implement
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")




def playerNextMove() -> None:
    """ prompts the player for a valid cell number, 
        and prints the info and the updated board;
        error checks that the input is a valid cell number 
    """
    #To Implement
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if move < 0 or move > 8 or move in played:
                print("Must enter a valid cell number.")
            else:
                board[move] = 'X'
                played.add(move)
                printBoard()
                break  # Valid move, break the loop
        except ValueError:
            print("Must enter a valid number between 0 and 8.")

def computerNextMove() -> None:
    """Computer randomly chooses a valid cell, updates the board, and prints the info."""
    while True:
        move = random.randint(0, 8)
        if move not in played:
            board[move] = 'O'  # Computer is always 'O'
            played.add(move)    # Add move to the set of played moves
            print(f"Computer chose: {move}")
            printBoard()        # Print updated board
            break


def hasWon(who: str) -> bool:
    """Returns True if 'who' ('X' or 'O') has won, False otherwise."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    # Check if any winning condition is met
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == who:
            return True
    return False


def terminate(who: str) -> bool:
    """ returns True if who (being passed 'X' or 'O') has won or if it's a draw, False otherwise;
        it also prints the final messages:
                "You won! Thanks for playing." or 
                "You lost! Thanks for playing." or 
                "A draw! Thanks for playing."  
    """
    #To Implement
    def terminate(who: str) -> bool:
        """Returns True if the game is over and prints the result."""
        if hasWon(who):
            if who == 'X':
                print("You won! Thanks for playing.")
            else:
                print("You lost! Thanks for playing.")
            return True
        elif len(played) == 9:  # All cells filled
            print("A draw! Thanks for playing.")
            return True
        return False



if __name__ == "__main__":
    # Use as is. 
    init()
    while True:
        playerNextMove()            # X starts first
        if(terminate('X')): break   # if X won or a draw, print message and terminate
        computerNextMove()          # computer plays O
        if(terminate('O')): break   # if O won or a draw, print message and terminate
